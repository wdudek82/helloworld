# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 18:54
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20160730_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 20, 54, 40, 947700)),
        ),
        migrations.AlterField(
            model_name='hello',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
