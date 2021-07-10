from typing import Optional, Any
import datetime
import json

import requests
from celery import shared_task

from apps.tender import models
from config.setting.config import CONFIG


@shared_task()
def fetch_data(datetime_day: Optional[str] = None,
               organization: Optional[str] = None) -> None:
    """Fetch data from National Grid ESO and store them into the database
    Args:
        datetime_day (Optional[str]): Define time for selection
            (in format YYYY-MM-DD), if None takes today
        organization (Optional[str]): Name of the organization.
    Note:
        - This has to be a Celery task (because there is a risk of time-outs)
    """
    # Set datetime_day to today if needed
    if datetime_day is None:
        # Set value to today value
        datetime_day = datetime.datetime.today().strftime('%Y-%m-%d')
    # Set organization for selection query
    if organization is None:
        organization = CONFIG.NGE_DEFAULT_ORGANIZATON
    # Define selection logic:
    request_params = {
        'resource_id': CONFIG.NGE_RESOURCE_ID,
        'q': json.dumps(
            {
                "Agent/Applicant": organization,
                "Delivery Date": datetime_day
            }
        )
    }
    # Get the response (send request with parameters):
    req = requests.get(CONFIG.NGE_BASE_URL, params=request_params)
    if req.status_code != 200:
        # In the case of error
        raise RuntimeError("error occurs during the process")

    # Extract data from request
    data = req.json()
    # Again, check if results were fetched correctly now on input level
    if not data['success']:  # Anticipate True
        # In the case of error
        raise RuntimeError("error occurs during the process")

    # Extract records:
    records: dict = data['result']['records']

    # Insert values to database
    for record in records:
        # Parse values in records (and map them to field names in db
        insert_fields: dict[str, Any] = {}
        for field in models.AuctionResults._meta.fields:
            try:
                insert_fields[field.name] = record.pop(field.help_text)
            except KeyError:
                # In the case when field is missing
                insert_fields[field.name] = None
        # Save values to database:
        auc_res = models.AuctionResults(**insert_fields)
        auc_res.save()
        # Now save additional fields:
        for name, value in record.items():
            auc_additional = models.AdditionalInfo(
                auction_result=auc_res,
                name=name,
                value=value
            )
            auc_additional.save()
