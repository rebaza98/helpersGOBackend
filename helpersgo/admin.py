# from django.contrib import admin
# from .models import *
# # Register your models here.
# admin.site.register(Servicio)
# admin.site.register(SubServicio)


from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TipoDocumento)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Telefono)
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Direccion)
admin.site.register(Servicio)
admin.site.register(SubServicio)
admin.site.register(Pedido)
admin.site.register(Proveedor_Servicio)