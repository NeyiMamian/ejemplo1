from django import forms
from .models import *


class contacto_form(forms.Form):
	correo= forms.EmailField(widget= forms.TextInput())
	tema= forms.CharField(widget= forms.TextInput())
	texto= forms.CharField(widget= forms.Textarea())

class registrar_form(forms.Form):
	nombre= forms.CharField(widget=forms.TextInput())
	edad= forms.IntegerField(widget=forms.TextInput())
	"""fecha_nacimiento=forms.Datefield(widget=forms.TextInput())"""
	celular= forms.IntegerField(widget=forms.TextInput())
	"""forever_alone= forms.BooleanField()"""
	sexo=forms.CharField(widget=forms.TextInput())
	usuario=forms.CharField(widget=forms.TextInput())
	clave=forms.CharField(widget=forms.PasswordInput())
	correo=forms.EmailField(widget=forms.TextInput())


class agregar_producto_form(forms.ModelForm):
	class Meta:
		model= Producto
		fields = '__all__'
