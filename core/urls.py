"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='acesso/usuarios/login.html', next_page = 'home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', include('apps.home.urls')),
    path('acesso/', include('apps.acesso.urls')),
    path('calculos/', include('apps.calculos.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('processos/', include('apps.processos.urls')),
    path('servicos/', include('apps.servicos.urls')),
    path('sistema', include('apps.sistema.urls')),

    #  Libs
    re_path(r"^celery-progress/", include("celery_progress.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )