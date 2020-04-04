# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store, Service
from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView

from .forms import DropOffForm, PickupForm, ServiceForm
from .models import Order

FORMS = [
    ("services", ServiceForm),
    ("pickup", PickupForm),
    ("dropoff", DropOffForm)
]

TEMPLATES = {
    "services": "core/order.html",
    "pickup": "core/order-address.html",
    "dropoff": "core/order-address.html"
}


class OrderWizard(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render(self.request, 'core/orderconfirm.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


# view for user to monitor their order history
def orderhistory_view(request, *args, **kwargs):
    customer_orders = Order.objects.all()
    addresses = Address.objects.all()
    my_context = {"core": customer_orders, "address": addresses}
    return render(request, "core/orderhistory.html", my_context)


# view to confirm that the order was successfully placed
def orderconfirm_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "core/orderconfirm.html", my_context)


# view to allow user to choose their destination
def orderdestination_view(request, *args, **kwargs):
    my_context = {}
    print(request.GET)
    print(request.POST)
    return render(request, "core/orderdestination.html", my_context)


# view to allow user to track the progress of their order
def tracking_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    my_context = {}
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
