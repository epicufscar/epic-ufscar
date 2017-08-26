# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170824_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='status',
            field=models.CharField(choices=[('EB', 'Em Breve'), ('EA', 'Em Andamento'), ('EN', 'Finalizado')], max_length=2, verbose_name='status'),
        ),
    ]