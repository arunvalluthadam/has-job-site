# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0005_auto_20150627_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addemail',
            name='head_email',
        ),
        migrations.DeleteModel(
            name='HeadEmail',
        ),
        migrations.RemoveField(
            model_name='addnumber',
            name='head_number',
        ),
        migrations.DeleteModel(
            name='HeadNumber',
        ),
        migrations.RemoveField(
            model_name='addorganization',
            name='head_organization',
        ),
        migrations.DeleteModel(
            name='HeadOrganization',
        ),
        migrations.RemoveField(
            model_name='clientapplication',
            name='head_application',
        ),
        migrations.DeleteModel(
            name='HeadApplication',
        ),
    ]
