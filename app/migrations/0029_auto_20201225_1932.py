# Generated by Django 2.1.15 on 2020-12-25 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20201225_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workfromgmail_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workorder', models.CharField(blank=True, max_length=255, null=True)),
                ('opended', models.CharField(blank=True, max_length=255, null=True)),
                ('caller', models.CharField(blank=True, max_length=255, null=True)),
                ('service_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('problum', models.TextField(blank=True, null=True)),
                ('fm', models.TextField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('time_make', models.DateTimeField(default=datetime.datetime(2020, 12, 25, 19, 32, 3, 715472))),
                ('time_create', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'งาน work from gmail new ',
                'verbose_name_plural': 'รายละเอียดงาน work from gmail new',
                'db_table': 'Workfromgmail_new',
            },
        ),
        migrations.AlterField(
            model_name='workfromgmail',
            name='timestramp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 19, 32, 3, 714909)),
        ),
    ]
