from django.shortcuts import render
from .models import Order,Item,Order_Adress,FeedBack,Status,Service



def order_view(request, *args, **kwargs):
    my_context = {}
    my_context ["services"]= Service.objects.all()
    return render(request, "orders/order.html", my_context)




