from django import forms
from .models import Categoria, Producto, Mesa, Cliente, Pedido, DetallePedido
from django.contrib.auth.forms import UserCreationForm
from .models import Clientes, PersonalRestaurante

class ClienteRegistrationForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Clientes
        fields = ('username', 'telefono', 'password1', 'password2')

class PersonalRestauranteRegistrationForm(UserCreationForm):
    cargo = forms.CharField(max_length=100, required=True)

    class Meta:
        model = PersonalRestaurante
        fields = ('username', 'cargo', 'password1', 'password2')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'asientos']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['mesa', 'cliente', 'esta_pagado']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio']
