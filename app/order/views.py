
from calendar import c
from turtle import tilt
from django.shortcuts import render

from order.models import Order

# Create your views here.

def order(request):

    order = Order.objects.all()

    context = {
        'order': order
    }


    return render(request, 'order/order.html', context)

def orderList(request):

    orderList = Order.objects.all()

    context = {
        'orderList': orderList
    }

    return render(request, 'order/order_list.html', context)

def orderItem(request, id):

    orderItem = Order.objects.all()
    orderItemTitle = Order.objects.all()

    context = {
        'title': 'Product List',
        "orderItem": orderItem,
        "id": id,
        "orderItemTitle": orderItemTitle

    }

    return render(request, 'order/order_item.html', context)