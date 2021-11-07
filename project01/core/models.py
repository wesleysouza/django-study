from django.db import models

class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('stock')


class Cliente(models.Model):
    name = models.CharField('name', max_length=100)
    surname = models.CharField('surname', max_length=100)
    email = models.EmailField('E-mail', max_length=100) 

