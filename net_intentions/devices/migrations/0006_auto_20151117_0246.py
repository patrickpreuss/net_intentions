# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20151117_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='platform',
            field=models.ForeignKey(to='devices.Platform'),
        ),
        migrations.AlterField(
            model_name='device',
            name='role',
            field=models.ForeignKey(to='devices.Role'),
        ),
    ]
