from django.shortcuts import render


def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "index.html", my_context)


def main_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "mainpage.html", my_context)


def about_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "about.html", my_context)


def services_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "services.html", my_context)





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
    my_context = {}
    return render(request, "orders/orderhistory.html", my_context)
