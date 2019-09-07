# Generated by Django 2.2.4 on 2019-08-24 17:33

import datetime
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockURL', '0002_stockinfonse'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockinfonse',
            name='divident',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockinfonse',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
