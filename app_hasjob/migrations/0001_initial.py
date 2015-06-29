# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name': 'Add Email',
                'verbose_name_plural': 'Add Emails',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddJobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('candidate_submit', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to=b'uploads/logo', verbose_name='Image')),
                ('url', models.URLField()),
                ('twitter', models.URLField()),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name': 'Add Job Post',
                'verbose_name_plural': 'Add Job Posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddMailTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Add Mail Type',
                'verbose_name_plural': 'Add Mail Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Add Number',
                'verbose_name_plural': 'Add Numbers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddNumberTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Add Number Type',
                'verbose_name_plural': 'Add Number Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Add Organization',
                'verbose_name_plural': 'Add Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('application_website', models.URLField()),
                ('redirect_url', models.URLField()),
                ('notification_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Client Application',
                'verbose_name_plural': 'Client Applications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Client Type',
                'verbose_name_plural': 'Client Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('job_application', models.TextField()),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeadApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'HeadApplication',
                'verbose_name_plural': 'HeadApplications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeadEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Head Email',
                'verbose_name_plural': 'Head Emails',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeadNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Head Number',
                'verbose_name_plural': 'Head Numbers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeadOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Head Organization',
                'verbose_name_plural': 'Head Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Signup',
                'verbose_name_plural': 'Signup',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientapplication',
            name='Head_application',
            field=models.ForeignKey(to='app_hasjob.HeadApplication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientapplication',
            name='types',
            field=models.ForeignKey(to='app_hasjob.ClientTypes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addorganization',
            name='head_organization',
            field=models.ForeignKey(to='app_hasjob.HeadOrganization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addnumber',
            name='head_number',
            field=models.ForeignKey(to='app_hasjob.HeadNumber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addnumber',
            name='types',
            field=models.ForeignKey(to='app_hasjob.AddMailTypes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addjobpost',
            name='category',
            field=models.ForeignKey(to='app_hasjob.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addjobpost',
            name='types',
            field=models.ForeignKey(to='app_hasjob.Types'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addemail',
            name='head_email',
            field=models.ForeignKey(to='app_hasjob.HeadEmail'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addemail',
            name='types',
            field=models.ForeignKey(to='app_hasjob.AddMailTypes'),
            preserve_default=True,
        ),
    ]
