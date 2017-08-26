# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 04:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170821_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopdates',
            name='time',
        ),
        migrations.AddField(
            model_name='workshopdates',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 8, 21, 4, 16, 16, 223400, tzinfo=utc), verbose_name='horário de fim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshopdates',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 8, 21, 4, 16, 24, 66151, tzinfo=utc), verbose_name='horário de início'),
            preserve_default=False,
        ),
    ]