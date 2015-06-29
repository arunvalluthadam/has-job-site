# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0007_auto_20150628_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addjobcategory',
            options={'verbose_name': 'Add Job Category', 'verbose_name_plural': 'Add Job Categories'},
        ),
        migrations.AlterModelOptions(
            name='addjobtypes',
            options={'verbose_name': 'Add Job Type', 'verbose_name_plural': 'Add Job Types'},
        ),
        migrations.RenameField(
            model_name='addjobpost',
            old_name='name',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='category',
            field=models.ForeignKey(to='app_hasjob.AddJobCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='types',
            field=models.ForeignKey(to='app_hasjob.AddJobTypes'),
            preserve_default=True,
        ),
    ]
