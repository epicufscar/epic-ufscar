# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('description', models.TextField(verbose_name='descrição')),
                ('workshops', models.ManyToManyField(to='core.Members', verbose_name='workshops')),
            ],
            options={
                'verbose_name': 'trilha',
                'verbose_name_plural': 'trilhas',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('description', models.TextField(verbose_name='descrição')),
                ('duration', models.FloatField(verbose_name='carga horária estimada')),
                ('status', models.CharField(choices=[('EB', 'Em Breve'), ('EX', 'Em Execução'), ('FI', 'Finalizado')], max_length=2, verbose_name='Status')),
                ('helpers', models.ManyToManyField(blank=True, related_name='workshop_workshop_helpers', to='core.Members', verbose_name='auxiliares')),
                ('instructors', models.ManyToManyField(related_name='workshop_workshop_instructors', to='core.Members', verbose_name='instrutores')),
            ],
            options={
                'verbose_name': 'workshop',
                'verbose_name_plural': 'workshops',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='WorkshopDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='data')),
                ('time', models.TimeField(verbose_name='horário')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='local')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Workshop', verbose_name='workshop')),
            ],
            options={
                'verbose_name': 'workshop data',
                'verbose_name_plural': 'workshop datas',
            },
        ),
        migrations.CreateModel(
            name='WorkshopGuests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='email')),
                ('page', models.CharField(blank=True, max_length=100, verbose_name='web page')),
                ('notes', models.TextField(blank=True, verbose_name='anotações')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Workshop', verbose_name='workshop')),
            ],
            options={
                'verbose_name': 'workshop convidados',
                'verbose_name_plural': 'workshop convidados',
            },
        ),
        migrations.AlterModelOptions(
            name='planbenefit',
            options={'ordering': ['priority'], 'verbose_name': 'plano de apoio - benefício', 'verbose_name_plural': 'plano de apoio - benefícios'},
        ),
        migrations.AlterModelOptions(
            name='plantype',
            options={'verbose_name': 'plano de apoio - tipo', 'verbose_name_plural': 'plano de apoio - tipos'},
        ),
    ]
