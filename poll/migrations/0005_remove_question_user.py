# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20160813_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
    ]
