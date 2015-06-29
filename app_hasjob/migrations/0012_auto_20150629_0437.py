# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0011_addjobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='addorganization',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 6, 29, 4, 37, 18, 602520, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientapplication',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 6, 29, 4, 37, 21, 546213, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 6, 29, 4, 37, 25, 752579, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
