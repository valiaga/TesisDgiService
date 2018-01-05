# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0009_auto_20180104_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='maximo',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='minimo',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='requerido',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='campo',
            name='key',
            field=models.CharField(default='a', help_text='Este campo es único', max_length=100, verbose_name='Key'),
        ),
        migrations.AddField(
            model_name='campo',
            name='max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Max'),
        ),
        migrations.AddField(
            model_name='campo',
            name='min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Min'),
        ),
        migrations.AddField(
            model_name='campo',
            name='model',
            field=models.CharField(blank=True, help_text='Solo para selects', max_length=200, null=True, verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='campo',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='campo',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Required'),
        ),
        migrations.AddField(
            model_name='campo',
            name='type',
            field=models.CharField(choices=[('INPUT', 'Input'), ('TEXTAREA', 'Textarea'), ('PASSWORD', 'Password'), ('NUMBER', 'Number'), ('EMAIL', 'Email'), ('CHECKBOX', 'Checkbox'), ('RADIOBUTTON', 'Radio-button'), ('SELECT', 'Select'), ('BUTTON', 'Button'), ('SLIDER', 'Slider'), ('FILEINPUT', 'File-input'), ('SLIDETOGGLE', 'Slide-toggle'), ('DATE', 'Date'), ('DATETIMELOCAL', 'Date-time-local'), ('MONTH', 'Month'), ('TIME', 'Time'), ('URL', 'Url')], default='INPUT', max_length=15, verbose_name='Type'),
        ),
    ]
