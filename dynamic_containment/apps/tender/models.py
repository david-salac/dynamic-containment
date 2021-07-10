from django.db import models


class AuctionResults(models.Model):
    """Main model for storing auction results.
    Note:
        - This is just a first version, there is no restriction imposed on
        acceptable values for each field.
        - Value help_text must match to field in JSON structure
        - All fields are nullable (just for case something is missing)
    """
    market_name = models.CharField(max_length=32,
                                   help_text="Market Name",
                                   null=True)
    delivery_date = models.DateField(help_text="Delivery Date",
                                     null=True)
    unique_bid_number = models.CharField(max_length=128,
                                         primary_key=True,
                                         help_text="Unique bid number")
    response_unit = models.CharField(max_length=64,
                                     help_text="Response Unit",
                                     null=True)
    unit_type = models.CharField(max_length=16,
                                 help_text="Unit type",
                                 null=True)
    agent_applicant = models.CharField(max_length=128,
                                       help_text="Agent/Applicant",
                                       null=True)
    related_entity = models.CharField(max_length=128,
                                      help_text="Related Entity",
                                      null=True)
    volume_offered = models.IntegerField(help_text="Volume offered",
                                         null=True)
    volume_accepted = models.IntegerField(help_text="Volume Accepted",
                                          null=True)
    delivery_start = models.DateTimeField(help_text="Delivery Start",
                                          null=True)
    delivery_end = models.DateTimeField(help_text="Delivery End",
                                        null=True)
    service_duration = models.IntegerField(help_text="Service Duration",
                                           null=True)
    availability_fee = models.DecimalField(max_digits=18,
                                           decimal_places=2,
                                           help_text="Availability Fee",
                                           null=True)
    total_cost = models.DecimalField(max_digits=18,
                                     decimal_places=2,
                                     help_text="Total Cost",
                                     null=True)
    rtm_no_rtm = models.CharField(max_length=64,
                                  help_text="RTM/no RTM",
                                  null=True)
    accepted_rejected = models.CharField(max_length=128,
                                         help_text="Accepted/Rejected",
                                         null=True)
    rejection_code = models.CharField(max_length=128,
                                      help_text="Rejection code",
                                      null=True)
    technology_type = models.CharField(max_length=128,
                                       help_text="Technology Type",
                                       null=True)
    rank_delivery_date = models.FloatField(help_text="rank Delivery Date",
                                           null=True)
    rank_agent_applicant = models.FloatField(help_text="rank Agent/Applicant",
                                             null=True)


class AdditionalInfo(models.Model):
    """This model represents additional columns that might come
    with bid results.
    """
    auction_result = models.ForeignKey(to=AuctionResults,
                                       on_delete=models.CASCADE,
                                       related_name="additional_files")
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=256)
