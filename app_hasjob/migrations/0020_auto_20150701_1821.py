# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0019_auto_20150701_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjobpost',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addorganization',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientapplication',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
