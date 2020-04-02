# noinspection PyUnresolvedReferences
from addresses.models import Address
from django.shortcuts import render, redirect

from .models import Order


# view for user to monitor their order history
def orderhistory_view(request, *args, **kwargs):
    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    my_context = {"orders": customer_orders, "address": addresses}
    return render(request, "orders/orderhistory.html", my_context)


# view to confirm that the order was successfully placed
def orderconfirm_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "orders/orderconfirm.html", my_context)


# view to allow user to choose their destination
def orderdestination_view(request, *args, **kwargs):
    my_context = {}
    print(request.GET)
    print(request.POST)
    return render(request, "orders/orderdestination.html", my_context)


# view to allow user to track the progress of their order
def tracking_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    my_context = {}
    return render(request, "orders/tracking.html", my_context)


# view to be presented if a user does not have any active orders
def no_order_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")

    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    status = Order.get_status()
    my_context = {"orders": customer_orders, "address": addresses, "status": status}
    return render(request, "orders/no_order_to_track.html", my_context)


# view commented out pending adjustment
"""def vieworder_view(request, *args, **kwargs):
    my_context = {}
    my_context = {
        "item": request.POST
    }

    order = Order()
    order.account = request.user
    order.pickup_time = request.POST.get('pickup_time')
    order.dropoff_time = request.POST.get('dropoff_time')
    order.save()
    ordersDetails = OrderDetails()
    ordersDetails.order = Order.objects.get(id=order.id)
    ordersDetails.service = Service.objects.get(service_name=request.POST.get('name'))
    ordersDetails.quantity = request.POST.get('quantity')
    adreespickup = Address()
    adreespickup.order = Order.objects.get(id=order.id)
    adreespickup.street = request.POST.get('street')
    adreespickup.city = request.POST.get('city')
    adreespickup.state = request.POST.get('state')
    adreespickup.zipcode = request.POST.get('zipcode')
    adreesdrop = Address()
    adreesdrop.order = Order.objects.get(id=order.id)
    adreesdrop.street = request.POST.get('streetD')
    adreesdrop.city = request.POST.get('cityD')
    adreesdrop.state = request.POST.get('stateD')
    adreesdrop.zipcode = request.POST.get('zipcodeD')
    status = Status()
    status.order = Order.objects.get(id=order.id)

    ordersDetails.save()
    adreespickup.save()
    adreesdrop.save()
    status.save()
    return render(request, "orders/vieworder.html", my_context)
"""