# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('admin', '0001_initial'),
        ('app_hasjob', '0001_initial'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='company_signup',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Company_signup',
        ),
        migrations.RemoveField(
            model_name='employee_signup',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Employee_signup',
        ),
    ]
