# Generated by Django 4.0.5 on 2022-10-22 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 22, 23, 19, 2, 374511)),
        ),
    ]
