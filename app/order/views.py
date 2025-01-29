
from calendar import c
from turtle import tilt
from django.shortcuts import render

from order.models import Order
from order.models import OrderList

# Create your views here.

def order(request):

    order = Order.objects.all()

    context = {
        'order': order
    }


    return render(request, 'order/order.html', context)

def orderList(request):

    orderList = OrderList.objects.all()

    context = {
        'orderList': orderList
    }

    return render(request, 'order/order_list.html', context)

def orderItem(request, id):

    orderItem = Order.objects.all()
    order_title = OrderList.objects.all()

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