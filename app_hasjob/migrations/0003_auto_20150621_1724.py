# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0002_auto_20150621_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemail',
            name='head_email',
            field=models.ForeignKey(blank=True, to='app_hasjob.HeadEmail', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='heademail',
            name='head',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
