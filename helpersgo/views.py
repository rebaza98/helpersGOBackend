from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

def index(request):
  #  return HttpResponse("Index")
    return render(request, 'helpersgo/index.html')

class ServicioApiView(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class SubServicioApiView(viewsets.ModelViewSet):
    queryset = SubServicio.objects.all()
    serializer_class = SubServicioSerializer