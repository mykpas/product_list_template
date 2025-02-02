
from django.shortcuts import render

from goods.models import  Products

# Create your views here.

def index(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:

        goods = Products.objects.filter(category__slug=category_slug)
            
    context = {
            'goods': goods
        }    

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    
    }

    return render(request, 'goods/product.html', context)