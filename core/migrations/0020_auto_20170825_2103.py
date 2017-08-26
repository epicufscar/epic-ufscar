# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170825_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='status',
            field=models.CharField(choices=[('EB', 'Em Breve'), ('EA', 'Em Andamento'), ('EN', 'Encerrado')], max_length=2, verbose_name='status'),
        ),
    ]