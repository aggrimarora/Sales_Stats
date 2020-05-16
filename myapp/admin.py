from django.contrib import admin
from .models import SalesRep, Product, Order

# Register your models here.
admin.site.register(SalesRep)
admin.site.register(Product)
admin.site.register(Order)
