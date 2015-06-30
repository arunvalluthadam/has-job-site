# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0014_auto_20150629_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='addjobpost',
            name='location',
            field=models.ForeignKey(to='app_hasjob.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
