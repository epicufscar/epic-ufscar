# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170822_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectionprocess',
            name='notes',
            field=models.TextField(default='', verbose_name='texto da página'),
            preserve_default=False,
        ),
    ]
