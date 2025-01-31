from django.contrib import admin

# Register your models here.
from .models import CarBrand, CarModel, Order, OrderHead

admin.site.register(Order)

admin.site.register(OrderHead)

admin.site.register(CarBrand)

admin.site.register(CarModel)


