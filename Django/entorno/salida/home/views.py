from django.shortcuts import render, redirect
from .forms import *
from .models import *

def vista_about(request):
	return render(request,'about.html')

def vista1_ejercito(request):
	return render(request,'ejercito.html')

def vista2_ejercicio1(request):
	return render(request,'ejercicio1.html')
# Create your views here.

def vista_contacto(request):
	info_enviado= False
	email= ""
	subject= ""
	text= ""
	if request.method== "POST":
		formulario=contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado= True
			email= formulario.cleaned_data['correo']
			subject=formulario.cleaned_data['tema']
			text=formulario.cleaned_data['texto']
			return render(request, 'contacto.html' , locals())
	else:
		formulario= contacto_form()
	return render(request, 'contacto.html',locals())

def vista_registrar(request):
	infor_enviado= False
	name= ""
	age= ""
	"""birth_date="""
	cell_phone=""
	"""foalone="""
	sex=""
	user=""
	key=""
	mail=""

	if request.method== "POST":
		trabajo=registrar_form(request.POST)
		if trabajo.is_valid():
			infor_enviado= True
			name= trabajo.cleaned_data['nombre']
			age= trabajo.cleaned_data['edad']
			"""date= trabajo.cleaned_data['fechanacimiento']"""
			cell_phone= trabajo.cleaned_data['celular']
			"""foalone= trabajo.cleaned_data['forever_alone']"""
			sex= trabajo.cleaned_data['sexo']
			user= trabajo.cleaned_data['usuario']
			key= trabajo.cleaned_data['clave']
			email= trabajo.cleaned_data['correo']
			return render(request, 'registrar.html' , locals())
	else:
		 trabajo = registrar_form()
	return render(request, 'registrar.html',locals())


def vista_pagina(request):
	return render(request,'pagina.html')

def vista_lista_producto(request):
	lista = Producto.objects.filter()
	return render(request,'Lista_de_producto.html', locals())

def vista_marca(request):
	M = Marca.objects.filter()
	return render(request,'Marcas.html', locals())

def vista_categoria(request):
	M = Categoria.objects.filter()
	return render(request,'Categoria.html', locals())

def vista_agregar_producto(request):
	if request.method =='POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form()
	return render(request,'vista_agregar_producto.html',locals())
		

	

def vista_ver_producto(request, id_prod):
	P = Producto.objects.get(id=id_prod)
	return render(request,'ver_producto_html',locals())
	