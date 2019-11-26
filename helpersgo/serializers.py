from rest_framework import serializers
from .models import *

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id', 'nombre', 'descripcion', 'activo')

class SubServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServicio
        fields = ('id', 'nombre', 'descripcion', 'tarifa_aprox', 'activo')