# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170825_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopgroupclass',
            name='application',
            field=models.URLField(blank=True, max_length=100, verbose_name='link formulário'),
        ),
    ]
