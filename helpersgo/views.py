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
from django.views.generic import ListView
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


class ProveedoresList(ListView):
    model = Proveedor
    template_name = 'helpersgo/proveedoresList.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Proveedor.objects.filter(descripcion__icontains=query)
            return context
        else:
            context = Proveedor.objects.all().order_by('id')
            return context