"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from ProyectoFinal import settings
from ProyectoFinal.views import about, notfound
from Blog.views import ver_paginas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ver_paginas, name="verPagina"),
    path('about/',about, name="acercaDeMi" ),
    path('notfound/',notfound, name="notFound" ),
    path('pages/', include('Blog.url')),
    path('account/', include('account.url')),
    path('*/',notfound, name="notFound" ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ProyectoFinal.views.notfound'