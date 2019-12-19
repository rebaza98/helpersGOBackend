"""helpersGOBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from helpersgo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helpersgo/', include(('helpersgo.urls', 'helpersgo'), namespace='helpersgo')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/cliente/', ClienteSignUpView.as_view(), name='cliente_signup'),
    path('accounts/signup/proveedor/', ProveedorSignUpView.as_view(), name='proveedor_signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'helpersgo/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'helpersgo/logout.html'), name = 'logout'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
