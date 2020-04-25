# noinspection PyUnresolvedReferences
from django.conf.urls import url
from business.views import (
    staffhome_view,
    current_orders_view,
    general_info_view,
    store_orderhistory_view,
    inventory_view,
    orders_details_view,
    services_business_view,
    no_order_view,
    feedback_view,
    no_feedback_view,
    delete_order_item_function,
    delete_service_function,
    delete_item_function,
    delete_staff_function,
    business_staff_view,
    staff_view,

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
    path('storeorders/', store_orderhistory_view, name="storeorders"),
    path('services/', services_view, name="services"),
    path('ajax/load-names/', load_service_view, name='ajax_load_names'),
    path('services_business/', services_business_view, name="services_business"),
    path('no_order/',no_order_view,name="no_order"),
    path('feedback/',feedback_view,name="feedback"),
    path('no_feedback/',no_feedback_view,name="nofeedback"),
    path('business_staff/', business_staff_view, name="staff"),
    path('staff/', staff_view, name="currentstaff"),
    url(r'^delete/service/(?P<obj_id>[0-9]+)/$', delete_service_function, name='delete_service_view'),
    url(r'^delete/(?P<obj_id>[0-9]+)/$',delete_order_item_function, name='delete_order_item_view'),
    url(r'^delete/item/(?P<obj_id>[0-9]+)/$',delete_item_function, name='delete_item_view'),
    url(r'^delete/staff/(?P<obj_id>[0-9]+)/$',delete_staff_function, name='delete_staff_view')

]
