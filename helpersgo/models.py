# from django.db import models

# # Create your models here.
# #YO SOY ALEX CUMPA, intentanto cuarta vez!!

# class TipoDocumento(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Pais(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Ciudad(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Provincia(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
# class Distrito(models.Model):
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')


# class Telefono(models.Model):
#     numero = models.CharField(max_length=30)
#     tipo_choices = (('C', 'Cellular'), ('F', 'Fijo'))
#     tipo = models.CharField(max_length=1, choices= tipo_choices, default= 'C')
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Persona(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido_paterno = models.CharField(max_length=50)
#     apellido_materno = models.CharField(max_length=50)
#     tipo_documento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.PROTECT)
#     nro_documento = models.CharField(max_length=50)
#     fec_nacimiento = models.DateField()
#     email = models.EmailField()
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Cliente(models.Model):
#     usuario = models.CharField(max_length=30, unique= True)
#     password = models.CharField(max_length=100)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Proveedor(models.Model):
#     usuario = models.CharField(max_length=30, unique= True)
#     password = models.CharField(max_length=100)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

# class Direccion(models.Model):
#     persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.PROTECT)
#     pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.PROTECT)
#     ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.PROTECT)
#     provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.PROTECT)
#     distrito = models.ForeignKey(Distrito, null=False, blank=False, on_delete=models.PROTECT)
#     direccion = models.CharField(max_length=200)

# class Servicio(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=50)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

#     def __str__(self):
#         return self.nombre

# class SubServicio(models.Model):
#     servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.PROTECT)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length= 50)
#     tarifa_aprox = models.DecimalField(max_digits=12, decimal_places=2)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

#     def __str__(self):
#         return self.nombre


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#I MADE THIS CHANGE CARLOS 13:51
#I MADE THIS CHANGE CARLOS 14:13

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    domicilio = models.TextField()
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return "{}".format(self.username) 

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.PROTECT)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return self.usuario.username

class Proveedor(models.Model):
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.PROTECT)
    #tipo_documento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.PROTECT)
    nro_documento = models.CharField(max_length=50)
    foto = models.CharField(max_length= 200)
    oficio = models.CharField(max_length=100)
    comentario = models.TextField()
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    
    def __str__(self):
        return "{}".format(self.usuario)


class Pais(models.Model):
    codigo = models.CharField(max_length=2, unique = True)
    nombre = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    codigo_pais = models.ForeignKey(Pais, to_field='codigo', blank=False, null=False, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    ciudad = models.ForeignKey(Ciudad, blank=False, null=False, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    provincia = models.ForeignKey(Provincia, blank=False, null=False, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.nombre


"""class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.PROTECT)
    nro_documento = models.CharField(max_length=50)
    fec_nacimiento = models.DateField()
    
    domicilio = models.TextField()
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellido_paterno, self.apellido_materno)
"""

#Analizar multiples telefonos
class TipoTelefono(models.Model):
    nombre = models.CharField(max_length=100)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.nombre

class Telefono(models.Model):
    usuario = models.ForeignKey(Usuario, blank=False, null=False, on_delete=models.PROTECT)
    tipotelefono = models.ForeignKey(TipoTelefono, null=False, blank=False, on_delete=models.PROTECT)
    numero = models.CharField(max_length=30)
    tipo_choices = (('C', 'Cellular'), ('F', 'Fijo'))
    tipo = models.CharField(max_length=1, choices= tipo_choices, default= 'C')
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    
    def __str__(self):
        return self.numero



class TipoDomicilio(models.Model):
    nombre = models.CharField(max_length=100)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    alias = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.PROTECT)
    tipodomicilio = models.ForeignKey(TipoDomicilio, null=False, blank=False, on_delete=models.PROTECT)
    pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.PROTECT)
    provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.PROTECT)
    distrito = models.ForeignKey(Distrito, null=False, blank=False, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')
    def __str__(self):
        return self.alias
    

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    icono = models.CharField(max_length=200, null = True, blank = True)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return self.nombre

class SubServicio(models.Model):
    servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length= 50)
    tarifa_aprox = models.DecimalField(max_digits=12, decimal_places=2)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    def __str__(self):
        return self.nombre

# Arturo

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.PROTECT)
    fecha_ini = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    fecha_cont = models.DateTimeField()
    comentario = models.CharField(max_length=100)
    calificacion = models.SmallIntegerField()
    estado_choices = (('A', 'Activo'), ('I', 'Inactivo'), ('N', 'Negocioacion'), ('A', 'Anulado'))
    estado = models.CharField(max_length=1, choices= estado_choices, default= 'A')


# #NORMALIZAR CON SUBSERVICIO
# class Proveedor_Servicio(models.Model):
#     proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.PROTECT)
#     servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.PROTECT)
#     activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
#     activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

#     class Meta:
#         unique_together = ["proveedor", "servicio"]

class Proveedor_SubServicio(models.Model):
    proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.PROTECT)
    subservicio = models.ForeignKey(SubServicio, null=False, blank=False, on_delete=models.PROTECT)
    activo_choices = (('A', 'Activo'), ('I', 'Inactivo'))
    activo = models.CharField(max_length=1, choices= activo_choices, default= 'A')

    class Meta:
        unique_together = ["proveedor", "servicio", "subservicio"]

    def __str__(self):
        return "{} -> {} -> {}".format(self.proveedor, self.servicio, self.subservicio)

