from operator import attrgetter

from accounts.models import Account
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store, Service
from business.views import get_order_queryset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from formtools.wizard.views import SessionWizardView

# noinspection PyUnresolvedReferences
from alora import settings
from .forms import DropOffForm, PickupForm, StoreForm
from .models import Order

ORDERS_PER_PAGE = 10

FORMS = [
    ("store", StoreForm),
    ("pickup", PickupForm),
    ("dropoff", DropOffForm)
]

TEMPLATES = {
    "store": "core/place-order.html",
    "pickup": "core/place-order.html",
    "dropoff": "core/place-order.html"
}


class OrderWizard(SessionWizardView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        self.storage.reset()
        self.storage.current_step = self.steps.first
        return super(OrderWizard, self).get(request, *args, **kwargs)

    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        if step == 'dropoff':
            step2 = self.get_cleaned_data_for_step('pickup')
            res = super(OrderWizard, self).get_form_initial(step)
            res['context'] = {}
            res['context']['pickup_date'] = step2['pickup_at']
            return res

    def done(self, form_list, **kwargs):
        form_dict1 = self.get_cleaned_data_for_step('store')
        store = form_dict1.get('store')
        form_dict2 = self.get_cleaned_data_for_step('pickup')
        pickup_street = form_dict2.get('street')
        pickup_apt = form_dict2.get('apt')
        pickup_city = form_dict2.get('city')
        pickup_state = form_dict2.get('state')
        pickup_zip_code = form_dict2.get('zip_code')
        pickup_at = form_dict2.get('pickup_at')
        form_dict3 = self.get_cleaned_data_for_step('dropoff')
        dropoff_street = form_dict3.get('street')
        dropoff_apt = form_dict3.get('apt')
        dropoff_city = form_dict3.get('city')
        dropoff_state = form_dict3.get('state')
        dropoff_zip_code = form_dict3.get('zip_code')
        dropoff_at = form_dict3.get('drop_off_at')

        pickup_location, created = Address.objects.get_or_create(
            street=pickup_street,
            apt=pickup_apt,
            city=pickup_city,
            state=pickup_state,
            zip_code=pickup_zip_code
        )
        dropoff_location, created = Address.objects.get_or_create(
            street=dropoff_street,
            apt=dropoff_apt,
            city=dropoff_city,
            state=dropoff_state,
            zip_code=dropoff_zip_code
        )

        Order.objects.create(
            user=get_object_or_404(Account, pk=self.request.user.pk),
            store=store,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            pickup_at=pickup_at,
            dropoff_at=dropoff_at
        )
        self.storage.reset()
        self.storage.current_step = self.steps.first
        self.request.session['form-submitted'] = True
        return redirect('orderconfirm')


# view for user to monitor their order history
def orderhistory_view(request, *args, **kwargs):
    my_context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    order_qs = Order.objects.all().filter(user=request.user)
    if not order_qs.exists():
        return redirect('no-order')

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        my_context['query'] = str(query)
        search_order = []
        for order in get_order_queryset(query):
            if order.user == request.user:
                search_order.append(order)
        my_context['search_order'] = search_order
    addresses = Address.objects.all()

    customer_orders = sorted(get_order_queryset(query), key=attrgetter('created_at'), reverse=True)

    filtered_orders = []
    for order in customer_orders:
        if order.user_id == request.user.id:
            filtered_orders.insert(1, order)

    filtered_orders = sorted(filtered_orders, key=attrgetter('created_at'), reverse=True)
    my_context["address"] = addresses
    my_context["user"] = user

    page = request.GET.get('page', 1)
    order_paginator = Paginator(filtered_orders, ORDERS_PER_PAGE)

    try:
        filtered_orders = order_paginator.page(page)
    except PageNotAnInteger:
        filtered_orders = order_paginator.page(ORDERS_PER_PAGE)
    except EmptyPage:
        filtered_orders = order_paginator.page(order_paginator.num_pages)

    my_context["core"] = filtered_orders

    return render(request, "core/orderhistory.html", my_context)


# view to confirm that the order was successfully placed
def orderconfirm_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not request.session.get('form-submitted', False):
        return redirect('place-order')
    request.session['form-submitted'] = False
    return render(request, "core/orderconfirm.html")


# view to allow user to track the progress of their order
def tracking_view(request, *args, **kwargs):
    my_context = {}

    if not request.user.is_authenticated:
        return redirect("login")
    order_qs = Order.objects.all().filter(user=request.user)
    if not order_qs.exists():
        return redirect('no-order')
    search_order = None
    if request.GET:
        query = request.GET['q']
        my_context['query'] = query

        for order in tracking_search(query):
            if order.user == request.user:
                search_order = order

    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    status = Order.current_status
    my_context = {"core": customer_orders, "address": addresses, "status": status, "search_order": search_order}

    return render(request, "core/tracking.html", my_context)


# view to be presented if a user does not have any active core
def no_order_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")

    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    status = Order.current_status
    my_context = {"core": customer_orders, "address": addresses, "status": status}
    return render(request, "core/no_order_to_track.html", my_context)


def customer_details_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")

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
    return render(request, "core/customer_order_details.html", my_context)


# allows user to view order details after submitting
def vieworder_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")

    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    my_context = {"core": customer_orders, "address": addresses}
    return render(request, "core/vieworder.html", my_context)


def tracking_search(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Order.objects.filter(Q(id__icontains=q)).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))
