#from django.urls import path
#from .views import index

#urlpatterns = [
#    path('', index, name='index'),
#]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('entrada/', views.entrada, name='entrada'),
    path('cocteles/', views.cocteles, name='cocteles'),
    path('tragos/', views.tragos, name='tragos'),
    path('pizza/', views.pizza, name='pizza'),
    path('form/', views.form, name='form'),

    # URLs para Categoria
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/new/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/edit/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),

    # URLs para Producto
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/new/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/edit/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/delete/', views.ProductoDeleteView.as_view(), name='producto-delete'),

    # URLs para Mesa
    path('mesas/', views.MesaListView.as_view(), name='mesa-list'),
    path('mesas/new/', views.MesaCreateView.as_view(), name='mesa-create'),
    path('mesas/<int:pk>/edit/', views.MesaUpdateView.as_view(), name='mesa-update'),
    path('mesas/<int:pk>/delete/', views.MesaDeleteView.as_view(), name='mesa-delete'),

    # URLs para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/new/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/edit/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente-delete'),

    # URLs para Pedido
    path('pedidos/', views.PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/new/', views.PedidoCreateView.as_view(), name='pedido-create'),
    path('pedidos/<int:pk>/edit/', views.PedidoUpdateView.as_view(), name='pedido-update'),
    path('pedidos/<int:pk>/delete/', views.PedidoDeleteView.as_view(), name='pedido-delete'),

    # URLs para DetallePedido
    path('detalles-pedido/', views.DetallePedidoListView.as_view(), name='detallepedido-list'),
    path('detalles-pedido/new/', views.DetallePedidoCreateView.as_view(), name='detallepedido-create'),
    path('detalles-pedido/<int:pk>/edit/', views.DetallePedidoUpdateView.as_view(), name='detallepedido-update'),
    path('detalles-pedido/<int:pk>/delete/', views.DetallePedidoDeleteView.as_view(), name='detallepedido-delete'),
]
