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
    path('pedido/', views.pedido, name='pedido'),

]
