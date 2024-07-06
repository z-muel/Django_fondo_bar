from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Producto, Mesa, Cliente, Pedido, DetallePedido
from django.views.generic.edit import CreateView


# Vista para la página de inicio
def index(request):
    return render(request, 'cliente/index.html')

def entrada(request):
    return render(request, 'cliente/entrada.html')

def cocteles(request):
    return render(request, 'cliente/cocteles.html')

def tragos(request):
    return render(request, 'cliente/tragos.html')

def pizza(request):
    return render(request, 'cliente/pizza.html')

def form(request):
    return render(request, 'cliente/form.html')

def pedido(request):
    return render(request, 'cliente/pedido.html')

# Vistas para Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria-list')
    template_name = 'categoria/form.html'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria-list')
    template_name = 'categoria/form.html'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria-list')
    template_name = 'categoria/delete_confirmation.html'

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('producto-list')
    template_name = 'producto/form.html'

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('producto-list')
    template_name = 'producto/form.html'

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
    template_name = 'producto/delete_confirmation.html'

# Vistas para Mesa
class MesaListView(ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'

class MesaCreateView(CreateView):
    model = Mesa
    fields = ['numero', 'asientos']
    success_url = reverse_lazy('mesa-list')
    template_name = 'mesa/form.html'

class MesaUpdateView(UpdateView):
    model = Mesa
    fields = ['numero', 'asientos']
    success_url = reverse_lazy('mesa-list')
    template_name = 'mesa/form.html'

class MesaDeleteView(DeleteView):
    model = Mesa
    success_url = reverse_lazy('mesa-list')
    template_name = 'mesa/delete_confirmation.html'

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('cliente-list')
    template_name = 'cliente/form.html'

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('cliente-list')
    template_name = 'cliente/form.html'

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')
    template_name = 'cliente/delete_confirmation.html'

# Vistas para Pedido
class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido/pedido_list.html'

class PedidoCreateView(CreateView):
    model = Pedido
    fields = ['mesa', 'cliente', 'esta_pagado']
    success_url = reverse_lazy('pedido-list')
    template_name = 'pedido/form.html'

class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ['mesa', 'cliente', 'esta_pagado']
    success_url = reverse_lazy('pedido-list')
    template_name = 'pedido/form.html'

class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido-list')
    template_name = 'pedido/delete_confirmation.html'

# Vistas para DetallePedido
class DetallePedidoListView(ListView):
    model = DetallePedido
    template_name = 'detallepedido/detallepedido_list.html'

class DetallePedidoCreateView(CreateView):
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio']
    success_url = reverse_lazy('detallepedido-list')
    template_name = 'detallepedido/form.html'

class DetallePedidoUpdateView(UpdateView):
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio']
    success_url = reverse_lazy('detallepedido-list')
    template_name = 'detallepedido/form.html'

class DetallePedidoDeleteView(DeleteView):
    model = DetallePedido
    success_url = reverse_lazy('detallepedido-list')
    template_name = 'detallepedido/delete_confirmation.html'
