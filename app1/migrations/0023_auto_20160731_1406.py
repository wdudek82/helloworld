# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20160731_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hello',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
