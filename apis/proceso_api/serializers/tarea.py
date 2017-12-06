"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso tarea.
"""
from apps.proceso.models.tarea import Tarea
from rest_framework import serializers


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'descripcion', 'plazo_dias', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
