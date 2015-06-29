# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0009_auto_20150629_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjobpost',
            name='date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='logo',
            field=models.ImageField(upload_to=b'uploads/logo', null=True, verbose_name='Image', blank=True),
            preserve_default=True,
        ),
    ]
