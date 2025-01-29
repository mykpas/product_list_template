from calendar import c
from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'
    verbose_name = 'Order'
    verbose_name_plural = 'Orders'


   