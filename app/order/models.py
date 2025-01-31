

from django.db import models

# Create your models here.

class Order(models.Model):

    user = models.CharField(max_length=50, verbose_name='Користувач', null=True, blank=True)
    product = models.CharField(max_length=50, verbose_name='Продукт', null=True, blank=True)
    serial = models.CharField(max_length=50, verbose_name='Номер', null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Кількість')
    invoce = models.CharField(max_length=50, verbose_name='Інвойс', null=True, blank=True)
    car_brand = models.CharField(max_length=50, verbose_name='Марка', null=True, blank=True)
    car_model = models.CharField(max_length=50, verbose_name='Модель', null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name='Колір', null=True, blank=True)
    create_time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)
    


    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Замовлення {}'.format(self.id)



class OrderHead(models.Model):

    date = models.DateField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)
    invoce = models.CharField(max_length=50, verbose_name='Інвойс' , null=True, blank=True)
    car_brand = models.CharField(max_length=50, verbose_name='Марка',   null=True, blank=True)
    car_model = models.CharField(max_length=50, verbose_name='Модель',  null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name='Колір',  null=True, blank=True)

    class Meta:
        verbose_name = 'шапка замовлення '  
        verbose_name_plural = 'шапка замовлень'

    def __str__(self):
        return 'шапка замовлення {}'.format(self.id)
    




class CarBrand(models.Model):
    name = models.TextField(max_length=50,  verbose_name='Марка', null=True, blank=True)

    class Meta:
        verbose_name = 'марка'  
        verbose_name_plural = 'марки'

    def __str__(self):
        return '{}'.format(self.name)

    

class CarModel(models.Model):

    manufacturer = models.ForeignKey(to=CarBrand, on_delete=models.CASCADE, verbose_name='Марка', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Модель', null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name='Колір', null=True, blank=True)
    invoice = models.CharField(max_length=50, verbose_name='Інвойс', null=True, blank=True)

    class Meta:
        verbose_name = 'Модель'  
        verbose_name_plural = 'Моделі'

    def __str__(self):
        return ' {}'.format(self.name)
    
