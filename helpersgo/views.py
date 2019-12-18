# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import *
# from .serializers import *

# # Create your views here.

# def index(request):
#   #  return HttpResponse("Index")
#     return render(request, 'helpersgo/index.html')

# class ServicioApiView(viewsets.ModelViewSet):
#     queryset = Servicio.objects.all()
#     serializer_class = ServicioSerializer

# class SubServicioApiView(viewsets.ModelViewSet):
#     queryset = SubServicio.objects.all()
#     serializer_class = SubServicioSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
  #  return HttpResponse("Index")
    return render(request, 'helpersgo/index.html')

def index2(request):
  #  return HttpResponse("Index")
    return render(request, 'helpersgo/index2.html')

class TipoDocumentoApiView(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class PaisApiView(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class CiudadApiView(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class ProvinciaApiView(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class DistritoApiView(viewsets.ModelViewSet):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class TelefonoApiView(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer

class PersonaApiView(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ClienteApiView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProveedorApiView(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class DireccionApiView(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class ServicioApiView(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class SubServicioApiView(viewsets.ModelViewSet):
    queryset = SubServicio.objects.all()
    serializer_class = SubServicioSerializer
  
class PedidoApiView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class Proveedores_SubServicioList(ListView):
    model = Proveedor_SubServicio
    template_name = 'helpersgo/proveedoresList.html'
    paginate_by = 10



    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        proveedor_value = Proveedores_ServicioList.objects.only('cod_insumo').get(pk=self.kwargs['pk']).cod_insumo
        context['mov_insumos'] = Cad_stock.objects.all().filter(cod_insumo=cadinsumo_value)
        # context['saldo'] = cantidad_mov_ingresos_suma['cantidad_mov__sum'] - cantidad_mov_salida_suma['cantidad_mov__sum']
        # print (context)
        return context
"""
    def get_context_data(self, **kwargs):
        servicioid = self.kwargs.get('pk', 0)
        print("pk")
        print(servicioid)
        context = super(Proveedores_SubServicioList, self).get_context_data(**kwargs)
        #Analizar Relacion
        prov_servicios = Proveedor_SubServicio.objects.values_list('proveedor', flat=True).filter(servicio=servicioid).order_by('id').distinct()
        for key in prov_servicios:
            print(key)
        print("provservicios")
        print(prov_servicios)
        provedores = Proveedor.objects.filter(id__in=prov_servicios)
        print("provedores")
        print(context)
        context['provedores'] = provedores
        personasDict = {}
        personasList = []
        for key in provedores:
            subservicios = Proveedor_SubServicio.objects.values_list('subservicio', flat=True).filter(proveedor=key.id).order_by('id').distinct()
            subservicios = SubServicio.objects.values_list('nombre', flat=True).filter(id__in=subservicios)
            print(key.persona)
            key.persona.comentario = key.comentario
            key.persona.subservicios = subservicios
            print("key.comentario")
            print(key.comentario)
            print(key.persona.comentario)
            print("key.persona.subservicios")
            print(key.persona.subservicios)
            print("SUBSERV")
            print(subservicios)
            personasList.append(key.persona)
#        context['proveedores']
        #print(context['proveedores'])
        context['personas'] = personasList
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Proveedor.objects.filter(descripcion__icontains=query)
            return context
        else:
            context = Proveedor.objects.all().order_by('id')
            return context
   


class Proveedor_Detail(DetailView):
    print("READ THIS")
    model = Persona
    template_name = 'helpersgo/proveedoresDetail.html'
    
    def get_context_data(self, **kwargs):
        personaid = self.kwargs.get('pk', 0)

        print("pk")
        print(personaid)
        context = super(Proveedor_Detail, self).get_context_data(**kwargs)
        personaobj =self.model.objects.get(id=personaid)
        proveedorobj = Proveedor.objects.get(persona=personaid)
        direccionobj = Direccion.objects.get(persona=personaid)
        telefonoobj = Telefono.objects.get(persona=personaid)
        #Da error cuando no hay objeto , añadir excepcion o cambiar comando
        direccionlst = Direccion.objects.filter(persona=personaid)
        for key in direccionlst:
            if key.tipodomicilio.nombre == "Principal":
                direccionobj = key        
        telfonolst = Telefono.objects.filter(persona=personaid)
        for key in telfonolst:
            if key.tipotelefono.nombre == "Principal":
                telefonoobj = key        
        print("direc")
        print(direccionobj)
        print("telefonoobj")
        print(telefonoobj)
        #Error de assignament before 
        context['persona'] = personaobj
        context['direccion'] = direccionobj
        context['telefono'] = telefonoobj
        context['proveedor'] = proveedorobj
        return context


class ContactoProveedor(TemplateView):
    print("This view is working")
    template_name = 'helpersgo/contactoProveedor.html'

    def get(self, request, *args, **kwargs):
        personaid = self.kwargs.get('pk', 0)
        print("PErsona id ",personaid)
        personaobj =Persona.objects.get(id=personaid)
        print("Yeah this works when page is loaded")
        subject = "Chambita detectada!!!"
        message = 'EL cliente tiene este problema : Caño malogrado /nContactarse con el atra vez de la webApp'
        fromEmail = settings.EMAIL_HOST_USER
        tomail = [personaobj.email]
        print("from")
        print("from")
        send_mail(subject, message, fromEmail, tomail, fail_silently=False)
                    
        # Explicitly states what get to call:
        return TemplateView.get(self, request, *args, **kwargs)

class BandejatareasList(ListView):
    model = Pedido
    template_name = 'helpersgo/bandejatareas.html'
    paginate_by = 10

class tareasdetalle(DetailView):
    model = Pedido
    template_name = 'helpersgo/tareasdetalle.html'
    paginate_by = 10

    
