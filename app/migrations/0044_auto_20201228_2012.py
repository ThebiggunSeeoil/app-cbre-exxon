# Generated by Django 2.1.15 on 2020-12-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_wahsubmitforcontractor_initials_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wahsubmitforcontractor',
            name='completedwork',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wahsubmitforcontractor',
            name='startwork',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]