

from os import name
import re
from django.shortcuts import redirect, render


from goods.models import Products
from order.models import CarBrand, CarModel, Order
from order.models import OrderHead

# Create your views here.


def order(request):

    order = Order.objects.all()
    header = OrderHead.objects.all()


    car_brand = CarBrand.objects.all()
   

    car_model = CarModel.objects.all()


    
    context = {
        'order': order,
        'header': header,
        'car_brand': car_brand,
        'car_model': car_model

    }

    return render(request, 'order/order.html', context)



def order_add(request, product_slug):

    product = Products.objects.get(slug = product_slug)
    exists_product = Order.objects.filter(product=product)

    if exists_product.exists():
        exists_product.update(quantity=exists_product[0].quantity + 1)
        
        return redirect(request.META.get('HTTP_REFERER'))

    Order.objects.create(product=product, serial=product.code,  quantity=1)

    return redirect(request.META.get('HTTP_REFERER'))    




def order_delete(request, product_id):

    Order.objects.filter(id=product_id).delete()

    return redirect(request.META.get('HTTP_REFERER'))





def orderList(request):

    orderList = OrderHead.objects.all()

   

    context = {
        'orderList': orderList,
       
    }

    return render(request, 'order/order_list.html', context)

def orderItem(request, id):

    orderItem = Order.objects.all()
    order_title = OrderHead.objects.all()

    for i in order_title:
        if i.id == id: 
            order_title = i 

    context = {
        'title': 'Product List',
        "orderItem": orderItem,
        "id": id,
        "order_title": order_title

    }

    return render(request, 'order/order_item.html', context)