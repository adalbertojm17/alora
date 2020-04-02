from django.urls import path, include
# noinspection PyPackageRequirements,PyUnresolvedReferences

from core.views import (
    tracking_view,
    no_order_view,
    orderhistory_view

)

urlpatterns = [
    path('tracking/', tracking_view, name="tracking"),
    path('noOrder/', no_order_view, name="No Order"),
    path('orderHistory/', orderhistory_view, name="Order History"),
]

