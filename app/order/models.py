
from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    code = models.CharField(max_length=50, verbose_name='Code')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Quantity')
    date = models.DateField(auto_now_add=True)
    invoce = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)
