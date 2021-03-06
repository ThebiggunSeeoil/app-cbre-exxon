# Generated by Django 2.1.15 on 2020-11-17 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.IntegerField()),
                ('pbl', models.IntegerField()),
                ('internal_order', models.IntegerField()),
                ('name', models.CharField(max_length=255, unique=True)),
                ('regiter_name', models.CharField(max_length=255, unique=True)),
                ('eng_name', models.CharField(max_length=255, unique=True)),
                ('area', models.CharField(max_length=255, unique=True)),
                ('tm', models.CharField(max_length=255)),
                ('am', models.CharField(max_length=255)),
                ('moso', models.CharField(max_length=255)),
                ('moso_type', models.CharField(max_length=255)),
                ('cat_type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'สถานี',
                'verbose_name_plural': 'ข้อมูลสถานี',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WorkPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('opended', models.DateTimeField()),
                ('startwork', models.DateTimeField()),
                ('completedwork', models.DateTimeField()),
                ('caller', models.CharField(max_length=255)),
                ('building_location', models.CharField(max_length=255)),
                ('service_provider', models.CharField(max_length=255)),
                ('equipment_code', models.CharField(max_length=255)),
                ('failure_code', models.CharField(max_length=255)),
                ('problem_code', models.CharField(max_length=255)),
                ('work_type', models.CharField(max_length=255)),
                ('problum', models.TextField(blank=True)),
                ('workorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SiteList')),
            ],
            options={
                'verbose_name': 'งานค้าง',
                'verbose_name_plural': 'รายละเอียดงานค้าง',
                'db_table': 'WorkPending',
            },
        ),
    ]
