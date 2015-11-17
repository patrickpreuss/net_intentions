# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20151117_0112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviceRole',
            new_name='Platform',
        ),
        migrations.RenameModel(
            old_name='DevicePlatform',
            new_name='Role',
        ),
    ]
