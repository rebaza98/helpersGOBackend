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
#router.register('persona',PersonaApiView)
router.register('cliente',ClienteApiView)
router.register('proveedor',ProveedorApiView)
router.register('direccion',DireccionApiView)
router.register('servicios', ServicioApiView)
router.register('subservicios', SubServicioApiView)
router.register('pedido', PedidoApiView)

urlpatterns = [
    url(r'^$', index, name='index'),
    url('prueba/', index2, name='index2'),
    url('listarPorveedor/(?P<pk>\d+)/$', Proveedores_SubServicioList.as_view(), name='proveedoresList'),
    url('listarPorveedor/detalleProveedor/(?P<pk>\d+)/$', Proveedor_Detail.as_view(), name='proveedoresDetail'),
    url('listarPorveedor/detalleProveedor/contactoProveedor/(?P<pk>\d+)/$', ContactoProveedor.as_view(), name='contactoProveedor'),
    url('listarTarea/', BandejatareasList.as_view(), name='listarTarea'),
    #url('crearPersona/', PersonaCreateView.as_view(), name='crearPersona'),
    
    path('apis/', include(router.urls))
]
