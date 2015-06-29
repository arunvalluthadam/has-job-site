# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0010_auto_20150629_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjobpost',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 6, 29, 3, 58, 35, 409822, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
