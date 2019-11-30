# from django.conf.urls import url
# from django.urls import path, include
# from .views import *
# from rest_framework import routers  
# # Cad_un_med_List, Cad_un_med_Create, Cad_un_med_Detail, Cad_un_med_Update, Cad_un_med_Delete

# router = routers.DefaultRouter()
# router.register('servicios', ServicioApiView)
# router.register('subservicios', SubServicioApiView)

# urlpatterns = [
#     url(r'^$', index, name='index'),
#     path('apis/', include(router.urls))
# ]



from django.conf.urls import url
from django.urls import path, include
from .views import *
from rest_framework import routers  
# Cad_un_med_List, Cad_un_med_Create, Cad_un_med_Detail, Cad_un_med_Update, Cad_un_med_Delete

router = routers.DefaultRouter()
router.register('tipodocumento',TipoDocumentoApiView)
router.register('pais',PaisApiView)
router.register('ciudad',CiudadApiView)
router.register('provincia',ProvinciaApiView)
router.register('distrito',DistritoApiView)
router.register('telefono',TelefonoApiView)
router.register('persona',PersonaApiView)
router.register('cliente',ClienteApiView)
router.register('proveedor',ProveedorApiView)
router.register('direccion',DireccionApiView)
router.register('servicios', ServicioApiView)
router.register('subservicios', SubServicioApiView)
router.register('pedido', PedidoApiView)

urlpatterns = [
    url(r'^$', index, name='index'),
    url('prueba/', index2, name='index2'),
    url('listarPorveedor/(?P<pk>\d+)/$', Proveedores_ServicioList.as_view(), name='proveedoresList'),
    path('apis/', include(router.urls))
]
