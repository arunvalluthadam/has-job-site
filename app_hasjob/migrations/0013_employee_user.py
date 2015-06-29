# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0012_auto_20150629_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, to='app_hasjob.Signup'),
            preserve_default=False,
        ),
    ]
