# noinspection PyUnresolvedReferences
from business.views import (
    staffhome_view,
    current_orders_view,
    general_info_view,
    staff_view,
    store_orderhistory_view,
    inventory_view,
    orders_details_view
)
from django.urls import path

urlpatterns = [
    path('currentorders/', current_orders_view, name="currentorders"),
    path('generalinfo/', general_info_view, name="generalinfo"),
    path('home/', staffhome_view, name="staffhome"),
    path('order_details/', orders_details_view, name="order_details"),
    path('staff/', staff_view, name="staff"),
    path('storeorders/', store_orderhistory_view, name="storeorders"),
]
