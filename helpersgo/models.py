from django.db import models

# Create your models here.


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
class Distrito(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')


class Telefono(models.Model):
    numero = models.CharField(max_length=30)
    tipo_choices = (('C', 'Cellular'), ('F', 'Fijo'))
    tipo = models.CharField(max_length=1, choices= tipo_choices, default= 'C')
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.PROTECT)
    nro_documento = models.CharField(max_length=50)
    fec_nacimiento = models.DateField()
    email = models.EmailField()
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Cliente(models.Model):
    usuario = models.CharField(max_length=30, unique= True)
    password = models.CharField(max_length=100)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Proveedor(models.Model):
    usuario = models.CharField(max_length=30, unique= True)
    password = models.CharField(max_length=100)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

class Direccion(models.Model):
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.PROTECT)
    pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.PROTECT)
    provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.PROTECT)
    distrito = models.ForeignKey(Distrito, null=False, blank=False, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)

class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')