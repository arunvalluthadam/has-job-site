# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0018_auto_20150701_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjobcategory',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobtypes',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
