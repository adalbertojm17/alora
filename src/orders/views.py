from django.shortcuts import render
from .models import Order,Item,Status,Service,OrderDetails,Adress
from  .forms import OrderDetailsForm


def load_service_view(request):
    service = request.GET.get('type')
    serviceNames = Service.objects.values_list('serviceName',flat=True).filter(serviceType=service)
    return render(request, 'orders/serviceName_dropdown_list_options.html', {'serviceNames': serviceNames})

def order_view(request, *args, **kwargs):

    form = OrderDetailsForm(request.POST or None)
    my_context = {
        'form':form
    }
    return render(request, "orders/order.html", my_context)

def orderconfirm_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "orders/orderconfirm.html", my_context)


def orderdestination_view(request, *args, **kwargs):
    my_context = {}
    print(request.GET)
    print(request.POST)
    return render(request, "orders/orderdestination.html", my_context)


def vieworder_view(request, *args, **kwargs):
    my_context = {}
    my_context= {
      "item": request.POST
     }

    order=Order()
    order.account = request.user
    order.pickupTime = request.POST.get('pickupTime')
    order.dropoffTime = request.POST.get('DropoffTime')
    order.save()
    ordersDetails = OrderDetails()
    ordersDetails.order= Order.objects.get(id = order.id)
    ordersDetails.service = Service.objects.get(serviceName= request.POST.get('name'))
    ordersDetails.quantity = request.POST.get('quantity')
    adreespickup = Adress()
    adreespickup.order=Order.objects.get(id = order.id)
    adreespickup.street = request.POST.get('street')
    adreespickup.city = request.POST.get('city')
    adreespickup.state = request.POST.get('state')
    adreespickup.zipcode = request.POST.get('zipcode')
    adreesdrop = Adress()
    adreesdrop.order =Order.objects.get(id = order.id)
    adreesdrop.street =request.POST.get('streetD')
    adreesdrop.city =request.POST.get('cityD')
    adreesdrop.state = request.POST.get('stateD')
    adreesdrop.zipcode = request.POST.get('zipcodeD')
    status = Status()
    status.order = Order.objects.get(id = order.id)

    ordersDetails.save()
    adreespickup.save()
    adreesdrop.save()
    status.save()


    return render(request, "orders/vieworder.html", my_context)


def orderhistory_view(request, *args, **kwargs):
    orders_order= Order.objects.all()
    my_context = {}
    return render(request, "orders/orderhistory.html", my_context)


