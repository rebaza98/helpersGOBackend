from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


# class CrearPersonaForm(forms.ModelForm):

#     class Meta:
#         model = Persona

#         fields = [
#             'nombre',
#             'apellido_paterno',
#             'apellido_materno',
#             'tipo_documento',
#             'nro_documento',
#             'fec_nacimiento',
#             'email',
#             'domicilio',
#             'activo',

#         ]
#         labels = {
#             'nombre': 'Nombre',
#             'apellido_paterno' : 'Apellido Paterno',
#             'apellido_materno' : 'Apellido Materno',
#             'tipo_documento' : 'Tipo de Documento',
#             'nro_documento' : 'Numero de Documento',
#             'fec_nacimiento' : 'Fecha de Nacimiento',
            
#             'domicilio' : 'Domicilio',
#             'activo' : 'Activo',
#         }
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
#             'apellido_paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
#             'apellido_materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Materno"}),
#             'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
#             'nro_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Numero de Documento"}),
#             'fec_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder':"Fecha de Nacimiento", 'type': 'date'}),
            
#             'domicilio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Domicilio"}),
#             'activo': forms.Select(attrs={'class': 'form-control'}),
#         }



# class CrearCliente(forms.ModelForm):

#     class Meta:
#         model = Cliente

#         fields = [
#             #'persona',
#             'usuario',
#             'password',
#             'email',
#             'activo',

#         ]
#         labels = {
#             #'persona': 'Persona',
#             'usuario' : 'Usuario',
#             'password' : 'Password',
#             'email' : 'Email',
#             'activo' : 'Activo',
#         }
#         widgets = {
#             #'Persona': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
#             'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
#             'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Email"}),
#             'activo': forms.Select(attrs={'class': 'form-control'}),
#         }

# class CrearProveedor(forms.ModelForm):

#     class Meta:
#         model = Proveedor

#         fields = [
#             'persona',
#             'usuario',
#             'foto',
#             'password',
#             'oficio',
#             'comentario',
#             'activo',

#         ]
#         labels = {
#             'persona': 'Persona',
#             'usuario' : 'Usuario',
#             'foto' : 'Foto',
#             'password' : 'Password',
#             'oficio' : 'Oficio',
#             'comentario' : 'Comentario',
#             'activo' : 'Activo',
#         }
#         widgets = {
#             'persona': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
#             'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
#             'foto': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Materno"}),
#             'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
#             'oficio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Numero de Documento"}),
#             'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Domicilio"}),
#             'activo': forms.Select(attrs={'class': 'form-control'}),
#         }

class ClienteSignUpForm(UserCreationForm):
    # nombre = forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
    # apellidos = forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
    # email = forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Email"}),
    # domicilio = forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Domicilio"}),
    # activo = forms.Select(attrs={'class': 'form-control'}),
    

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields #+ ('nombre', 'apellidos', 'email', 'domicilio')
        fields += (
            'nombre',
            'apellidos',
            'email',
            'domicilio',
            'activo',

        )
        labels = {
            'nombre' : 'Nombre:',
            'apellidos' : 'Apellidos:',
            'email' : 'Email:',
            'domicilio' : 'Domicilio:',
            'activo' : 'Activo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Email"}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Domicilio"}),
            'activo': forms.Select(attrs={'class': 'form-control'}),
        }

    @transaction.atomic
    def save(self):
        usuario = super().save(commit=False)
        usuario.is_client = True
        usuario.save()
        cliente = Cliente.objects.create(usuario=usuario)
        return usuario


class ProveedorSignUpForm(UserCreationForm):
    #tipo_documento_id = forms.ModelChoiceField(queryset=TipoDocumento.objects.all(),required=True,widget=forms.Select(attrs={'class': 'form-control'}),label="Tipo de Documento:")
    nro_documento = forms.Field(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Numero de Documento"}),label="Nro Documento")
    foto = forms.Field(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Url de FOto"}),label="Foto:")
    oficio = forms.Field(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Oficio"}),label="Oficio:")
    comentario = forms.Field(required=True,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa algo sobre ti"}),label="Comentario:")

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields #+ ('nombre', 'apellidos', 'email', 'domicilio')
        fields += (
            'nombre',
            'apellidos',
            'email',
            'domicilio',
            'activo',

        )
        labels = {
            'nombre' : 'Nombre:',
            'apellidos' : 'Apellidos:',
            'email' : 'Email:',
            'domicilio' : 'Domicilio:',
            'activo' : 'Activo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Nombre"}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Apellido Paterno"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Email"}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Ingresa tu Domicilio"}),
            'activo': forms.Select(attrs={'class': 'form-control'}),
        }
    @transaction.atomic
    def save(self):
        print("debugwwwww************")
        usuario = super().save(commit=False)
        usuario.is_provider = True
        usuario.save()
       # print(self.cleaned_data.get('tipo_documento_id'))
        
        #proveedor.tipo_documento_id.add(self.cleaned_data.get('tipo_documento_id'))
        nro_documento = self.cleaned_data.get('nro_documento')
        foto = self.cleaned_data.get('foto')
        oficio = self.cleaned_data.get('oficio')
        comentario = self.cleaned_data.get('comentario')
        proveedor = Proveedor.objects.create(usuario=usuario, nro_documento = nro_documento, foto = foto, oficio = oficio, comentario = comentario)
        return usuario
    