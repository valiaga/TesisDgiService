# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0008_auto_20180104_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='orden',
            field=models.IntegerField(blank=True, null=True, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='orden',
            field=models.IntegerField(blank=True, null=True, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='flex',
            field=models.IntegerField(blank=True, default=100, help_text='width in %', null=True, verbose_name='Flex'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='hint_end_count_text',
            field=models.BooleanField(default=False, help_text='texto de ayúda Count del letras en el Input.', verbose_name='Hint_end_count_text'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='hint_start',
            field=models.CharField(blank=True, help_text='Texto de ayúda.', max_length=200, null=True, verbose_name='Hint_start'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='json',
            field=models.TextField(blank=True, help_text='Solo para selects', null=True, verbose_name='Json'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='modelo',
            field=models.CharField(blank=True, help_text='Solo para selects', max_length=200, null=True, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='multiselect',
            field=models.NullBooleanField(default=False, help_text='Solo para selects', verbose_name='Multiselect'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='name',
            field=models.CharField(help_text='Este campo es único', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='prefix',
            field=models.CharField(blank=True, help_text='Útil para campos codigos telefonicos que van antes del numero. ej. 051, 054', max_length=50, null=True, verbose_name='Prefix'),
        ),
    ]