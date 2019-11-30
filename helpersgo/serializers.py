# from rest_framework import serializers
# from .models import *

# class ServicioSerializer(serializers.ModelSerializer):
#     print("Estamos aqui")

#     class Meta:
#         model = Servicio
#         fields = ('id', 'nombre', 'descripcion', 'activo')

# class SubServicioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubServicio
#         fields = ('id', 'nombre', 'descripcion', 'tarifa_aprox', 'activo')

from rest_framework import serializers,viewsets
from .models import TipoDocumento, Pais, Ciudad, Provincia, Distrito, Telefono, Persona, Cliente, Proveedor, Direccion, Servicio, SubServicio, Pedido

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ['nombre', 'descripcion', 'activo_choices', 'activo']

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'descripcion', 'activo_choices', 'activo']

class CiudadSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'descripcion', 'activo_choices', 'activo']

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['nombre', 'descripcion', 'activo_choices', 'activo']

class DistritoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ['nombre', 'descripcion', 'activo_choices', 'activo']

class TelefonoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ['numero', 'tipo_choices', 'tipo', 'activo_choices', 'activo']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'tipo_documento', 'nro_documento', 'fec_nacimiento', 
                    'email', 'activo_choices', 'activo']

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['usuario', 'password', 'activo_choices', 'activo']

class ProveedorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['usuario', 'password', 'activo_choices', 'activo']

class DireccionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['persona', 'pais', 'ciudad', 'provincia', 'distrito', 'direccion']

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'descripcion', 'activo']

class SubServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServicio
        fields = ['id', 'servicio', 'nombre', 'descripcion', 'tarifa_aprox', 'activo']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['cliente', 'proveedor', 'fecha_ini', 'fecha_fin', 'fecha_cont', 'comentario', 'calificacion']