from django.urls import path

from .views import (
    tracking_view,
    no_order_view,
    orderhistory_view,
    # vieworder_view,
    orderconfirm_view,
    OrderWizard,

)

urlpatterns = [
    path('tracking/', tracking_view, name="tracking"),
    path('no-order/', no_order_view, name="no-order"),
    path('order-history/', orderhistory_view, name="order-history"),
    path('place-order/', OrderWizard.as_view(), name="orderconfirm"),
    path('order-confirm/', orderconfirm_view, name="orderconfirm"),
    path('tracking/', tracking_view, name="tracking"),
    # path('vieworder/', vieworder_view, name="vieworder"),
]
