# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Order
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import ServiceCreationForm
from .models import Service
from.models import Store
from core.models import Item


def orders_details_view(request, *args, **kwargs):
    order_id = request.GET.get('order')
    order = Order.objects.get(id=order_id)
    my_context = {
        'order': order,
        'orderdetails': order.orderitem_set.all()
    }

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/orders_details.html", my_context)


def staffhome_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/home.html", my_context)


def current_orders_view(request, *args, **kwargs):
    my_context = {
        'core': Order.objects.all()
    }

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/current_orders.html", my_context)


def general_info_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/general_info.html", my_context)


def staff_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/staff.html", my_context)


def store_orderhistory_view(request, *args, **kwargs):
    my_context = {
        'orders': Order.objects.all()
    }
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/store_orderhistory.html", my_context)


def inventory_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/inventory.html", my_context)


def services_view(request):
    service = request.GET.get('type')
    service_names = Service.objects.values_list('name', flat=True).filter(store=service)
    return render(request, 'services.html', {'service_names': service_names})


def load_service_view(request):
    service = request.GET.get('type')
    service_names = Service.objects.values_list('service_name', flat=True).filter(serviceType=service)
    return render(request, 'orders/serviceName_dropdown_list_options.html', {'service_names': service_names})


def services_view(request):
    context = {}
    store = Store.objects.get(manager= request.user)
    service = Service.objects.get(store= store)
    items = Item.objects.get(service=service)
    context={
        'services':service,
        'items':items
    }
    if request.POST:
        form = ServiceCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ServiceCreationForm()

    context ['form']=form

    return render(request, 'business/services.html', context)

