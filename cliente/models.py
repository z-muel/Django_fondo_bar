from django.contrib.auth.models import AbstractUser
from django.db import models

class Clientes(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username  # O cualquier otro campo que desees mostrar como representación del usuario

class PersonalRestaurante(AbstractUser):
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.username  # O cualquier otro campo que desees mostrar como representación del usuario


# Modelo para almacenar las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la categoría
    descripcion = models.TextField(blank=True)  # Descripción de la categoría (opcional)

    def __str__(self):
        return self.nombre  # Devuelve el nombre de la categoría cuando se imprime el objeto

# Modelo para almacenar los productos del menú
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField(blank=True)  # Descripción del producto (opcional)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con la categoría (clave foránea)

    def __str__(self):
        return self.nombre  # Devuelve el nombre del producto cuando se imprime el objeto

# Modelo para representar las mesas del restaurante
class Mesa(models.Model):
    numero = models.IntegerField(unique=True)  # Número de la mesa (único)
    asientos = models.IntegerField()  # Número de asientos en la mesa

    def __str__(self):
        return f"Mesa {self.numero}"  # Devuelve el número de la mesa cuando se imprime el objeto

# Modelo para almacenar la información de los clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    email = models.EmailField(blank=True)  # Correo electrónico del cliente (opcional)
    telefono = models.CharField(max_length=15, blank=True)  # Teléfono del cliente (opcional)

    def __str__(self):
        return self.nombre  # Devuelve el nombre del cliente cuando se imprime el objeto

# Modelo para almacenar los pedidos realizados
class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)  # Relación con la mesa (clave foránea)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el cliente (opcional)
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del pedido
    actualizado_en = models.DateTimeField(auto_now=True)  # Fecha y hora de la última actualización del pedido
    esta_pagado = models.BooleanField(default=False)  # Indicador de si el pedido está pagado

    def __str__(self):
        return f"Pedido {self.id} en {self.mesa}"  # Devuelve una representación del pedido cuando se imprime el objeto

# Modelo para almacenar los detalles de cada pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')  # Relación con el pedido (clave foránea)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el producto (clave foránea)
    cantidad = models.IntegerField()  # Cantidad del producto en el pedido
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto al momento del pedido

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"  # Devuelve una representación del detalle del pedido cuando se imprime el objeto

    def precio_total(self):
        return self.cantidad * self.precio  # Calcula el precio total de este detalle del pedido
