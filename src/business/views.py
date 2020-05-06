from operator import attrgetter

from accounts.models import Account
from core.models import Item
from core.models import Order
from core.models import OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from feedback.models import Feedback

from .forms import AddingItemForm
from .forms import AddingOrderItemForm
from .forms import ServiceCreationForm, ServiceAreasForm
from .forms import StaffCreationForm, DropOffUpdateForm
from .models import Service, ServingAreas
from .models import Store

ORDERS_PER_PAGE = 10


def staff_view(request, *args, **kwargs):
    try:
        my_context = {
            'staff': Store.objects.get(manager=request.user).staff.all
        }
    except ObjectDoesNotExist:
        return redirect('no_order')

    if not (Store.objects.get(manager=request.user).staff):
        return redirect('no_order')

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()

    return render(request, "business/current_staff.html", my_context)


def business_staff_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    if request.POST:
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            form.save()
            store = Store.objects.get(manager=request.user)
            store.staff.add(Account.objects.get(username=username))
            return redirect('currentstaff')
    else:
        form = StaffCreationForm()
    context = {
        'form': form
    }
    return render(request, 'business/business_staff.html', context)


def feedback_view(request, *args, **kwargs):
    try:
        my_context = {
            'feedback': Feedback.objects.all().filter(store=Store.objects.get(manager=request.user))
        }
    except ObjectDoesNotExist:
        return redirect('nofeedback')

    if not (Feedback.objects.all().filter(store=Store.objects.get(manager=request.user))):
        return redirect('nofeedback')

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()

    return render(request, "business/feedback.html", my_context)


def orders_details_view(request, *args, **kwargs):
    form = AddingOrderItemForm
    order_id = request.GET.get('order')
    order = Order.objects.get(id=order_id)
    price = 0
    for items in order.orderitem_set.all():
        price = price + items.quantity * items.item.price

    my_context = {
        'order': order,
        'orderdetails': order.orderitem_set.all(),
        'price': price
    }

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()

    if 'button1' in request.POST:
        form = AddingOrderItemForm(request.user, order, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/business/order_details/?order=' + str(order.id))
    else:
        form = AddingOrderItemForm(user=request.user, order=order)

    if 'button3' in request.POST:
        dropform = DropOffUpdateForm(request.POST, instance=order)
        if dropform.is_valid():
            print('1000000')
            dropform.save()
            return HttpResponseRedirect('/business/order_details/?order=' + str(order.id))
    else:
        dropform = DropOffUpdateForm()

    if 'button2' in request.POST:
        order.current_status = request.POST.get('status')
        order.save()

    my_context['form'] = form
    my_context['dropform'] = dropform

    return render(request, "business/orders_details.html", my_context)


def staffhome_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()
    return render(request, "business/home.html", my_context)


# noinspection DuplicatedCode
def current_orders_view(request, *args, **kwargs):
    my_context = {}
    if request.user.is_manager:
        try:
            my_context = {
                'orders': Order.objects.all().filter(store=Store.objects.get(manager=request.user))
            }
        except ObjectDoesNotExist:
            return redirect('no_order')

        if not (Order.objects.all().filter(store=Store.objects.get(manager=request.user))):
            return redirect('no_order')
    elif request.user.is_employee:
        try:
            my_context = {
                'orders': Order.objects.all().filter(store=Store.objects.get(staff=request.user))
            }
        except ObjectDoesNotExist:
            return redirect('no_order')

        if not (Order.objects.all().filter(store=Store.objects.get(staff=request.user))):
            return redirect('no_order')

    query = ""
    if request.GET:
        query = request.GET['q']
        my_context['query'] = query
        search_order = []
        for order in get_order_queryset(query):
            if order.store == Store.objects.get(manager=request.user):
                search_order.append(order)
        my_context['search_order'] = search_order

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()

    orders = []
    for order in get_order_queryset(query):
        if order.store == Store.objects.get(manager=request.user):
            orders.append(order)

    orders = sorted(orders, key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    order_paginator = Paginator(orders, ORDERS_PER_PAGE)

    try:
        orders = order_paginator.page(page)
    except PageNotAnInteger:
        orders = order_paginator.page(ORDERS_PER_PAGE)
    except EmptyPage:
        orders = order_paginator.page(order_paginator.num_pages)

    my_context["orders"] = orders

    return render(request, "business/current_orders.html", my_context)


def general_info_view(request, *args, **kwargs):
    my_context = {}

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    store = Store.objects.get(manager=request.user)

    my_context['seviceareas'] = store.servingareas.all
    if request.POST:
        form = ServiceAreasForm(request.POST)
        if form.is_valid():
            zip = form.cleaned_data['zipcode']
            form.save()
            store.servingareas.add(ServingAreas.objects.filter(zipcode=zip).first())
            return HttpResponseRedirect('/business/generalinfo/')
    else:
        form = ServiceAreasForm()
    my_context['form'] = form
    return render(request, "business/general_info.html", my_context)


# noinspection DuplicatedCode
def store_orderhistory_view(request, *args, **kwargs):
    my_context = {}
    if request.user.is_manager:
        try:
            my_context = {
                'orders': Order.objects.all().filter(store=Store.objects.get(manager=request.user))
            }
        except ObjectDoesNotExist:
            return redirect('no_order')

        if not (Order.objects.all().filter(store=Store.objects.get(manager=request.user))):
            return redirect('no_order')
    elif request.user.is_employee:
        try:
            my_context = {
                'orders': Order.objects.all().filter(store=Store.objects.get(staff=request.user))
            }
        except ObjectDoesNotExist:
            return redirect('no_order')

        if not (Order.objects.all().filter(store=Store.objects.get(staff=request.user))):
            return redirect('no_order')

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        my_context['query'] = query
        search_order = []
        for order in get_order_queryset(query):
            if order.store == Store.objects.get(manager=request.user):
                search_order.append(order)
                my_context['search_order'] = search_order

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager and not request.user.is_employee:
        return HttpResponseForbidden()

    orders = []
    for order in get_order_queryset(query):
        if order.store == Store.objects.get(manager=request.user):
            orders.append(order)

    orders = sorted(orders, key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    order_paginator = Paginator(orders, ORDERS_PER_PAGE)

    try:
        orders = order_paginator.page(page)
    except PageNotAnInteger:
        orders = order_paginator.page(ORDERS_PER_PAGE)
    except EmptyPage:
        orders = order_paginator.page(order_paginator.num_pages)

    my_context["orders"] = orders
    return render(request, "business/store_orderhistory.html", my_context)


def inventory_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    return render(request, "business/inventory.html", my_context)


def services_view(request):
    my_context = {}
    stores = Store.objects.all()
    my_context['stores'] = stores
    if request.GET:
        SerchStore = request.GET.get('company')
        if SerchStore != "":
            services = Service.objects.all().filter(store__name=SerchStore)
            items = []
            for service in services:
                items.append(Item.objects.all().filter(services=service))
            my_context['itemsQuery'] = items
            my_context['services'] = services
            my_context['company'] = Store.objects.get(name=SerchStore)
    return render(request, 'services.html', my_context)


def load_service_view(request):
    service = request.GET.get('type')
    service_names = Service.objects.values_list('service_name', flat=True).filter(serviceType=service)
    return render(request, 'core/serviceName_dropdown_list_options.html', {'service_names': service_names})


def services_business_view(request):
    context = {}
    try:
        store = Store.objects.get(manager=request.user)
        services = Service.objects.all().filter(store=store)
        items = []
        for service in services:
            items.append(Item.objects.all().filter(services=service))
        context['itemsQuery'] = items
        context['services'] = services
    except ObjectDoesNotExist:
        store = []

    if 'submit1' in request.POST:
        form = ServiceCreationForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/business/company_services/')

    else:
        form = ServiceCreationForm(user=request.user)

    context['form'] = form

    if 'submit2' in request.POST:
        form2 = AddingItemForm(request.user, request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect('/business/company_services/')


    else:
        form2 = AddingItemForm(user=request.user)

    context['form2'] = form2

    return render(request, 'business/services_business.html', context)


def get_order_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Order.objects.filter(Q(user__username__icontains=q) | Q(id__icontains=q)).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))


def no_order_view(request):
    return render(request, 'business/no_orders.html')


def no_feedback_view(request):
    return render(request, 'business/no_feedback.html')


def delete_order_item_function(request, obj_id=None):
    object = OrderItem.objects.get(id=obj_id)
    id = object.order.id
    object.delete()
    return HttpResponseRedirect('/business/order_details/?order=' + str(id))


def delete_service_function(request, obj_id=None):
    object = Service.objects.get(id=obj_id)
    object.delete()
    return HttpResponseRedirect('/business/company_services/')


def delete_item_function(request, obj_id=None):
    object = Item.objects.get(id=obj_id)
    object.delete()
    return HttpResponseRedirect('/business/company_services/')


def delete_staff_function(request, obj_id=None):
    object = Account.objects.get(id=obj_id)
    object.delete()
    return HttpResponseRedirect('/business/staff/')
