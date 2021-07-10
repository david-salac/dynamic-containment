from rest_framework import serializers

from apps.tender import models


class AuctionResultsSerializer(serializers.ModelSerializer):
    """Base serializer to data view (list/detailed view)"""
    class Meta:
        model = models.AuctionResults
        exclude = []


class FetchDataSerializer(serializers.Serializer):
    """Base serializer for data processing"""
    organization = serializers.CharField(max_length=128,
                                         allow_null=True,
                                         required=False)
    datetime_day = serializers.DateField(allow_null=True,
                                         required=False)
