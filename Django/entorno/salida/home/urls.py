from django .urls import path
from django.contrib import admin
from .views import*


urlpatterns = [
	path('admin/', admin.site.urls),
    path('about/', vista_about, name='vista_about'),
    path('ejercito/', vista1_ejercito, name='vista1_ejercito'),
    path('ejercicio1/', vista2_ejercicio1),
    path('contacto/', vista_contacto, name='vista_contacto'),
    path('registro/', vista_registrar),
    path('pagina/', vista_pagina),
    path('lista_producto/',vista_lista_producto, name='vista_lista_producto'),
    path('Marcas/', vista_marca, name='Marcas'),
    path('Categoria/', vista_categoria, name='categorias'),
    path('agregar_producto/', vista_agregar_producto, name='vista_agregar_producto'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name='vista_ver_producto'),
]


