# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0006_auto_20150628_0658'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Types',
            new_name='AddJobCategory',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='AddJobTypes',
        ),
        migrations.AlterModelOptions(
            name='addjobcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='addjobtypes',
            options={'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.RenameField(
            model_name='addjobcategory',
            old_name='types',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='addjobtypes',
            old_name='category',
            new_name='types',
        ),
        migrations.AddField(
            model_name='addjobpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 10, 39, 6, 745397, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addjobpost',
            name='headline',
            field=models.CharField(default=datetime.datetime(2015, 6, 28, 10, 39, 10, 368666, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
