# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 04:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0011_auto_20180105_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campo',
            options={'verbose_name': 'campo', 'verbose_name_plural': 'campos'},
        ),
        migrations.AddField(
            model_name='formulario',
            name='width',
            field=models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Width'),
        ),
    ]
