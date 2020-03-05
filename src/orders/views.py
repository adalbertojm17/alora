from django.shortcuts import render
from .models import Order,Item,Order_Adress,FeedBack,Status,Service



def order_view(request, *args, **kwargs):
    my_context = {}
    my_context ["services"]= Service.objects.all()
    return render(request, "orders/order.html", my_context)

def orderconfirm_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "orders/orderconfirm.html", my_context)


def orderdestination_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "orders/orderdestination.html", my_context)


def vieworder_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "orders/vieworder.html", my_context)


def orderhistory_view(request, *args, **kwargs):
    orders_order= Order.objects.all()
    my_context = {}
    return render(request, "orders/orderhistory.html", my_context)


