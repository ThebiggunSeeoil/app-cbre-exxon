# Generated by Django 2.1.15 on 2020-12-23 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20201223_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='workfromgmail',
            name='date_create',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workfromgmail',
            name='timestramp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 17, 56, 24, 931652)),
        ),
    ]