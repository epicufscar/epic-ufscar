# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_workshopdates_recurrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='status',
            field=models.CharField(choices=[('EB', 'Em Breve'), ('EX', 'Em Execução'), ('FI', 'Finalizado')], default='EB', max_length=2, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specialization',
            name='workshops',
            field=models.ManyToManyField(to='core.Workshop', verbose_name='workshops'),
        ),
    ]