# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20151113_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='hostname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='deviceplatform',
            old_name='platform',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='devicerole',
            old_name='role',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
    ]
