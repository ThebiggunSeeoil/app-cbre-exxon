# Generated by Django 2.1.15 on 2020-12-25 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20201225_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workfromgmail',
            name='timestramp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 19, 37, 47, 862257)),
        ),
        migrations.AlterField(
            model_name='workfromgmail_new',
            name='time_make',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 19, 37, 47, 862733)),
        ),
    ]
