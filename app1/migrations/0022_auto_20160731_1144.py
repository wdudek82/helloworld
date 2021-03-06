# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 09:44
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_delete_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='example',
            old_name='user',
            new_name='name',
        ),
        migrations.AddField(
            model_name='example',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 31, 9, 43, 39, 438922, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='example',
            name='flag',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='example',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 9, 44, 10, 120294, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='example',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 31, 9, 44, 18, 409327, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hello',
            name='flag',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
