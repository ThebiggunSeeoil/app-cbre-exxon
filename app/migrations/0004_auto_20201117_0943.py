# Generated by Django 2.1.15 on 2020-11-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201117_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitelist',
            name='area',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sitelist',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sitelist',
            name='regiter_name',
            field=models.CharField(max_length=255),
        ),
    ]
