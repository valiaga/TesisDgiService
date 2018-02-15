# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0018_auto_20180208_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='backgroud',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='key',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='max',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='min',
        ),
        migrations.AddField(
            model_name='campo',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text="Este campo es único 'is key' ", max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campo',
            name='placeholder',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Placeholder'),
        ),
    ]
