# Generated by Django 4.0.5 on 2022-10-23 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_date_orderplaced_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 23, 20, 9, 46, 81386)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 23, 20, 9, 46, 80382)),
        ),
    ]