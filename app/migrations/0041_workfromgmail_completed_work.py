# Generated by Django 2.1.15 on 2020-12-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20201225_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='workfromgmail',
            name='completed_work',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
