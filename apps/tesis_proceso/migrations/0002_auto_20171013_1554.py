# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesis_proceso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesisetapa',
            name='tesis_proceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesisetapa', to='tesis_proceso.TesisProceso', verbose_name='Tesis_proceso'),
        ),
        migrations.AddField(
            model_name='tesisrequisito',
            name='tesis_tarea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisito', to='tesis_proceso.TesisTarea', verbose_name='Tesis_tarea'),
        ),
        migrations.AddField(
            model_name='tesistarea',
            name='tesis_etapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesistarea', to='tesis_proceso.TesisEtapa', verbose_name='Tesis_etapa'),
        ),
        migrations.AlterField(
            model_name='tesisproceso',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de fin'),
        ),
    ]
