from django.contrib import admin

# Register your models here.
from .models import Order, OrderList

admin.site.register(Order)

admin.site.register(OrderList)


