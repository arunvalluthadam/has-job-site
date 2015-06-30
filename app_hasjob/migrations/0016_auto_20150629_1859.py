# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0015_auto_20150629_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addjobpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='addjobpost',
            name='location',
        ),
        migrations.RemoveField(
            model_name='addjobpost',
            name='types',
        ),
        migrations.DeleteModel(
            name='AddJobPost',
        ),
    ]
