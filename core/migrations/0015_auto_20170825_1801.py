# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170825_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshopgroupclass',
            options={'ordering': ['group'], 'verbose_name': 'workshop - turma', 'verbose_name_plural': 'workshops - turmas'},
        ),
    ]
