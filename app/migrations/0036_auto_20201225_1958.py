# Generated by Django 2.1.15 on 2020-12-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20201225_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workfromgmail_new',
            name='time_make',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
