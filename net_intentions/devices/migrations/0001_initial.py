# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=255)),
                ('management_ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='DevicePlatform',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('platform', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceRole',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('role', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('region', models.CharField(unique=True, max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_platform',
            field=models.ForeignKey(to='devices.DevicePlatform'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_role',
            field=models.ForeignKey(to='devices.DeviceRole'),
        ),
        migrations.AddField(
            model_name='device',
            name='region',
            field=models.ForeignKey(to='devices.Region'),
        ),
    ]
