# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170824_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='helpers',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='instructors',
        ),
    ]
