# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0008_auto_20150628_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjobpost',
            name='owner_name',
            field=models.CharField(default=datetime.datetime(2015, 6, 29, 2, 50, 8, 874500, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='candidate_submit',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='twitter',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
