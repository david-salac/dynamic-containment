import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import rest_framework.status as http_status

import apps.api.serializers.tender as serializers
from apps.tender.tasks import fetch_data
from apps.tender import models
from config.setting.config import CONFIG


class AuctionResultsViewSet(viewsets.ReadOnlyModelViewSet):
    """View set for display results"""
    serializer_class = serializers.AuctionResultsSerializer
    queryset = models.AuctionResults.objects.all()

    @action(methods=['post'],
            detail=False,
            url_path="fetch_data",
            url_name="fetch_data",
            serializer_class=serializers.FetchDataSerializer)
    def fetch_data(self, request, *args, **kwargs):
        """Run task that stores data in database.
        """
        f_data_ser = serializers.FetchDataSerializer(data=request.data,
                                                     context={
                                                         'request': request
                                                     })
        f_data_ser.is_valid(raise_exception=True)

        # Prepare data:
        organization = CONFIG.NGE_DEFAULT_ORGANIZATON
        datetime_day = datetime.datetime.today().strftime('%Y-%m-%d')
        if 'organization' in f_data_ser.validated_data:
            organization = str(f_data_ser.validated_data['organization'])
        if 'datetime_day' in f_data_ser.validated_data:
            datetime_day = str(f_data_ser.validated_data['datetime_day'])

        # Run the task that process request (run as asynchronous celery task)
        sgn = fetch_data.s(datetime_day, organization)
        sgn.delay()

        return Response(
            {
                'organization': organization,
                'datetime_day': datetime_day,
            },
            status=http_status.HTTP_200_OK
        )
