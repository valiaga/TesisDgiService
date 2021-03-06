# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-29 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0024_auto_20180727_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('alias', models.CharField(max_length=50, verbose_name='Alias')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('llave_documento', models.CharField(max_length=60, verbose_name='Llave documento')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
            },
        ),
    ]
