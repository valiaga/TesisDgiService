# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-12 06:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripción')),
                ('fecha_envio', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de envio')),
                ('fecha_leido', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de lectura')),
            ],
            options={
                'verbose_name': 'Observacion',
                'verbose_name_plural': 'Observaciones',
            },
        ),
        migrations.CreateModel(
            name='TesisEtapa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fecha fin')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisetapa', to='proceso.Etapa', verbose_name='Etapa')),
            ],
            options={
                'verbose_name': 'TesisEtapa',
                'verbose_name_plural': 'TesisEtapas',
            },
        ),
        migrations.CreateModel(
            name='TesisProceso',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('fecha_inicio', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('estado', models.CharField(choices=[('ACTIVO', 'Activo'), ('TERMINADO', 'Terminado'), ('ABANDONADO', 'Abandonado'), ('OTRO', 'Otro')], default='ACTIVO', max_length=15, verbose_name='Estado')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisproceso', to='proceso.Proceso', verbose_name='Proceso')),
            ],
            options={
                'verbose_name': 'TesisProceso',
                'verbose_name_plural': 'TesisProcesos',
            },
        ),
        migrations.CreateModel(
            name='TesisRequisito',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('estado', models.CharField(choices=[('VENCIDO', 'Vencido'), ('CUMPLIDO', 'Cumplido'), ('NO_CUMPLIDO', 'No cumplido')], default='NO_CUMPLIDO', max_length=15, verbose_name='Estado')),
                ('informacion_adicional', models.TextField(blank=True, null=True)),
                ('requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisito', to='proceso.Requisito', verbose_name='Requisito')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisito', to='proceso.Resultado', verbose_name='Resultado')),
            ],
            options={
                'verbose_name': 'TesisRequisito',
                'verbose_name_plural': 'TesisRequisitos',
            },
        ),
        migrations.CreateModel(
            name='TesisRequisitoArchivo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('archivo', models.FileField(default='tesis_requisito_archivo/archivos/none/default.pdf', upload_to='tesis_requisito_archivo/archivos/', verbose_name='Archivo')),
                ('imagen', models.ImageField(default='tesis_requisito_archivo/imagenes/none/default.png', upload_to='tesis_requisito_archivo/fotos/', verbose_name='Foto')),
                ('tesis_requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisitoarchivo', to='tesis_proceso.TesisRequisito', verbose_name='Tesis_requisito')),
            ],
            options={
                'verbose_name': 'TesisRequisitoArchivo',
                'verbose_name_plural': 'TesisRequisitoArchivos',
            },
        ),
        migrations.CreateModel(
            name='TesisTarea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha de finalizaciòn')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesistarea', to='proceso.Tarea', verbose_name='Tarea')),
            ],
            options={
                'verbose_name': 'TesisTarea',
                'verbose_name_plural': 'TesisTareas',
            },
        ),
    ]
