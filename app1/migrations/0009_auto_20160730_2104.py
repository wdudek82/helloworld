# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 19:04
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20160730_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='test_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 21, 4, 35, 402707)),
        ),
        migrations.AlterField(
            model_name='hello',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 21, 4, 35, 402644)),
        ),
    ]
