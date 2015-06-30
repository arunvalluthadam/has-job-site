# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hasjob', '0016_auto_20150629_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddJobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=200)),
                ('owner_name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('candidate_submit', models.TextField(null=True, blank=True)),
                ('company', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.ImageField(upload_to=b'uploads/logo', null=True, verbose_name='Image', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(to='app_hasjob.AddJobCategory')),
                ('location', models.ForeignKey(to='app_hasjob.Location')),
                ('types', models.ForeignKey(to='app_hasjob.AddJobTypes')),
            ],
            options={
                'verbose_name': 'Add Job Post',
                'verbose_name_plural': 'Add Job Posts',
            },
            bases=(models.Model,),
        ),
    ]
