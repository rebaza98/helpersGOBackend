from django.conf.urls import url
from django.urls import path, include
from .views import *
from rest_framework import routers  
# Cad_un_med_List, Cad_un_med_Create, Cad_un_med_Detail, Cad_un_med_Update, Cad_un_med_Delete

router = routers.DefaultRouter()
router.register('servicios', ServicioApiView)
router.register('subservicios', SubServicioApiView)

urlpatterns = [
    url(r'^$', index, name='index'),
    path('apis/', include(router.urls))
]

