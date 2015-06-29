# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0004_auto_20150627_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientapplication',
            name='head_application',
            field=models.ForeignKey(blank=True, to='app_hasjob.HeadApplication', null=True),
            preserve_default=True,
        ),
    ]
