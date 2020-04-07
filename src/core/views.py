# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
from accounts.models import Account
from addresses.models import Address
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store, Service
from django.shortcuts import render, redirect, get_object_or_404
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

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        return super(OrderWizard, self).get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        form_dict1 = self.get_cleaned_data_for_step(1)
        services = form_dict1.get('services')
        form_dict2 = self.get_cleaned_data_for_step(2)
        pickup_street = form_dict2.get('street')
        pickup_apt = form_dict2.get('apt')
        pickup_city = form_dict2.get('city')
        pickup_state = form_dict2.get('state')
        pickup_zip_code = form_dict2.get('zip_code')
        form_dict3 = self.get_cleaned_data_for_step(3)
        dropoff_street = form_dict3.get('street')
        dropoff_apt = form_dict3.get('apt')
        dropoff_city = form_dict3.get('city')
        dropoff_state = form_dict3.get('state')
        dropoff_zip_code = form_dict3.get('zip_code')
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
            state=dropoff_zip_code,
            zip_code=pickup_zip_code
        )

        order = Order.objects.get_or_create(
            account=get_object_or_404(Account, pk=self.request.user.pk),
            store=get_object_or_404(Store, pk=self.request.user.pk),

        )

        return redirect('main')


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
