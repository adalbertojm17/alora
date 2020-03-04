from django.shortcuts import render
from .models import Order,Item,Order_Adress,FeedBack,Status,Service

def service (request):
    allservices = Service.objects.all();
    return render(request,"order.html",allservices)






