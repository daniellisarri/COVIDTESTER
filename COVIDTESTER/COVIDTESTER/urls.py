"""COVIDTESTER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

# Importación de vistas
from AutoTest import views

# Un path por cada vista, + path vacío + admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('preAutoTest/', views.pre_auto_Test, name="preAutoTest"),
    path('AutoTest/', views.auto_Test, name="AutoTest"),
    path('resultado/', views.resultado, name="resultado"), 
    path('condiciones/', views.condiciones, name="condiciones"), 
    path('posible_positivo/', views.posible_positivo, name="posible_positivo"),
    path('negativo/', views.negativo, name="negativo"),
    path('contacto/', views.contacto, name="contacto"),
]