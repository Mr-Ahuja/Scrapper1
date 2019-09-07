from decimal import Decimal

from django.db import models
from datetime import date

# Create your models here.
class StockURL(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

class StockInfoNSE(models.Model):

    name = models.CharField(max_length=255)
    date = models.DateField( default=date.today)
    open = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    high = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    low = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    offer = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    divident = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    volume = models.IntegerField()
