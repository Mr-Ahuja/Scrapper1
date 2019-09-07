from decimal import Decimal
from datetime import date

from rest_framework import serializers

from .models import StockURL,StockInfoNSE

class StockURLSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return StockURL.objects.create(**validated_data)

class StockInfoNSESerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    date = serializers.DateField(default=date.today)
    open = serializers.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    high = serializers.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    low = serializers.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    offer = serializers.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    divident = serializers.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    volume = serializers.IntegerField()

    def create(self, validated_data):
        return StockInfoNSE.objects.create(**validated_data)