from django.conf.urls import url
from .views import *
# Cad_un_med_List, Cad_un_med_Create, Cad_un_med_Detail, Cad_un_med_Update, Cad_un_med_Delete

urlpatterns = [
    url(r'^$', index, name='index'),
]