from django import forms
from .models import Categoria, Producto, Mesa, Cliente, Pedido, DetallePedido


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
