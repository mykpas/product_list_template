
from turtle import color
from django.db import models

# Create your models here.

class Order(models.Model):
    product = models.CharField(max_length=50, verbose_name='Продукт')
    serial = models.CharField(max_length=50, verbose_name='Номер')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Кількість')
    


    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Замовлення {}'.format(self.id)

class OrderList(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    invoce = models.CharField(max_length=50, verbose_name='Інвойс')
    car_brand = models.CharField(max_length=50, verbose_name='Марка')
    car_model = models.CharField(max_length=50, verbose_name='Модель')
    color = models.CharField(max_length=50, verbose_name='Колір')

    class Meta:
        verbose_name = 'лист замовлення '  
        verbose_name_plural = 'листи замовлень'

    def __str__(self):
        return 'Замовлення {}'.format(self.id)