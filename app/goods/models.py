
from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категорія')
    slug = models.SlugField(max_length=50, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

class Products(models.Model):
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')
    name = models.CharField(max_length=50, verbose_name='Назва')
    slug = models.SlugField(max_length=50, verbose_name='Slug')
    quantity = models.IntegerField(default=0, verbose_name='Кількість')
    code = models.CharField(max_length=50, verbose_name='Код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'    
        verbose_name_plural = 'Товари'