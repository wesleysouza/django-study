from django.contrib import admin

from .models import Product, Cliente

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cliente, ClienteAdmin)
