# Generated by Django 2.1.15 on 2020-12-25 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20201225_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workfromgmail_new',
            name='time_make',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 19, 40, 1, 648564)),
        ),
    ]
