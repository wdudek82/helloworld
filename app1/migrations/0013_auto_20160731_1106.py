# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20160731_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 11, 6, 45, 12047)),
        ),
        migrations.AlterField(
            model_name='hello',
            name='test_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 11, 6, 45, 12106)),
        ),
    ]
