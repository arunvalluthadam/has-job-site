# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0003_auto_20150621_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientapplication',
            old_name='Head_application',
            new_name='head_application',
        ),
    ]
