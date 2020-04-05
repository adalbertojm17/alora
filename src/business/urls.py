# noinspection PyUnresolvedReferences
from business.views import (
    staffhome_view,
    current_orders_view,
    general_info_view,
    staff_view,
    store_orderhistory_view,
    inventory_view,
    orders_details_view,
    services_business_view
)
from django.urls import path

from .views import (
    services_view,
    load_service_view)

urlpatterns = [
    path('currentorders/', current_orders_view, name="currentorders"),
    path('generalinfo/', general_info_view, name="generalinfo"),
    path('home/', staffhome_view, name="staffhome"),
    path('order_details/', orders_details_view, name="order_details"),
    path('staff/', staff_view, name="staff"),
    path('storeorders/', store_orderhistory_view, name="storeorders"),
    path('services/', services_view, name="services"),
    path('ajax/load-names/', load_service_view, name='ajax_load_names'),
    path('services_business/', services_business_view, name="services_business"),

]
