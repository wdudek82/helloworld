# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 09:25
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20160731_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 11, 25, 16, 823281)),
        ),
        migrations.AlterField(
            model_name='hello',
            name='test_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 11, 25, 16, 823336)),
        ),
    ]
