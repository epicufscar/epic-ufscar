# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170821_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['title'], 'verbose_name': 'workshop', 'verbose_name_plural': 'workshops'},
        ),
    ]
