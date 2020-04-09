# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Order
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Store,Service
# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Item
from .forms import ServiceCreationForm
from .forms import AddingOrderItemForm
from .forms import AddingItemForm
from django.db.models import Q
from .models import Service
from accounts.forms import AccountForm
from accounts.models import Account


def orders_details_view(request, *args, **kwargs):
    form = AddingOrderItemForm
    order_id = request.GET.get('order')
    order = Order.objects.get(id=order_id)
    print(request.POST.get('status'))
    my_context = {
        'order': order,
        'orderdetails': order.orderitem_set.all()
    }

    if not request.user.is_authenticated:
        return redirect('login')
    elif not request.user.is_manager:
        return HttpResponseForbidden()
    if request.POST:
        form = AddingOrderItemForm(request.POST)
        order.current_status = request.POST.get('status')
        order.save()
        if form.is_valid():
            form.save()

    else:
        form = AddingOrderItemForm()

    my_context ['form']=form

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
        'orders': Order.objects.all()
    }
    query = " "
    if request.GET:
        query = request.GET['q']
        my_context['query'] = query

    SearchOrder = get_order_queryset(query)
    my_context['SearchOrder'] =SearchOrder

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
    query = " "
    if request.GET:
        query = request.GET['q']
        my_context['query'] = query
    SearchOrder = get_order_queryset(query)
    my_context['SearchOrder'] = SearchOrder

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
    my_context = {}
    stores = Store.objects.all()
    my_context['stores'] = stores

    SerchStore = request.GET.get('company')
    services =Service.objects.all().filter(store__name=SerchStore)
    items = []
    for service in services:
        items.append(Item.objects.all().filter(services=service))
    my_context['itemsQuery'] = items
    my_context['services'] = services
    return render(request, 'services.html', my_context)


def load_service_view(request):
    service = request.GET.get('type')
    service_names = Service.objects.values_list('service_name', flat=True).filter(serviceType=service)
    return render(request, 'core/serviceName_dropdown_list_options.html', {'service_names': service_names})

def services_business_view(request):
    context = {}
    store = Store.objects.get(manager= request.user)
    services = Service.objects.all().filter(store= store)
    items =[]
    for service in services:
        items.append(Item.objects.all().filter( services = service))
    context['itemsQuery']=items
    context['services']=services

    if request.POST:
        form = ServiceCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ServiceCreationForm()

    context ['form']=form

    if request.POST:
        form2 = AddingItemForm(request.POST)
        if form2.is_valid():
            form2.save()

    else:
        form2 = AddingItemForm()

    context ['form2']=form2


    return render(request, 'business/services_business.html', context)

def get_order_queryset(query= None):
    queryset =[]
    queires = query.split(" ")
    for q in queires:
        posts = Order.objects.filter(Q(account__username__icontains =q)|Q(id__icontains=q)).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

def business_account_view(request, *args, **kwargs):

    if not request.user.is_authenticated:
        return redirect("login")
    obj = Account.objects.get(id=request.user.id)
    context = {
        'phone': obj.phone,
        'user': request.user,
    }
    if request.POST:
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = AccountForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "phone": context['phone'],
                "email": request.user.email,
                "email2": request.user.email,
                "username": request.user.username,
            }
        )
    context["form"] = form



    return render(request, "business/business_account.html", context)