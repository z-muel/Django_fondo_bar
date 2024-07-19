from django.shortcuts import render
from django.urls import reverse_lazy

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

