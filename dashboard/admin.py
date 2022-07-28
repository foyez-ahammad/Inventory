from django.contrib import admin
from django.contrib.auth.models import Group, User
from . import models

# admin.site.unregister(Group)
admin.site.site_header = 'Inventory Dashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'category', 'quantity')
    list_filter = ['category', 'name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',  'staff', 'order_quantity', 'date')
    list_filter = ['product', 'staff', 'date']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
