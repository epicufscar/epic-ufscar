# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170821_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopdates',
            name='recurrent',
            field=models.BooleanField(default=False, verbose_name='recorrente'),
            preserve_default=False,
        ),
    ]
