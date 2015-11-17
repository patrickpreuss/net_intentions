# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20151115_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_platform',
            new_name='platform',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_role',
            new_name='role',
        ),
    ]
