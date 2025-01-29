from django.contrib import admin

# Register your models here.

from .models import Categories, Products



@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'id')

@admin.register(Products)    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    
    list_display = ('name', 'slug', 'id')
