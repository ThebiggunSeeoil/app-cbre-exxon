# Generated by Django 2.1.15 on 2020-11-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201117_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpending',
            name='completedwork',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workpending',
            name='startwork',
            field=models.CharField(max_length=255),
        ),
    ]
