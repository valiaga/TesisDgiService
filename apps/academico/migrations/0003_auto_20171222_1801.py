# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_lineainvestigacion_escuela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='logo',
            field=models.ImageField(blank=True, default='escuela/logos/none/default.png', null=True, upload_to='escuela/logos/', verbose_name='Logo'),
        ),
    ]