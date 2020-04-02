# noinspection PyPackageRequirements,PyUnresolvedReferences
from core.views import (
    tracking_view,
    no_order_view,
    orderhistory_view,
    place_order_view,
    add_item_view
)
from django.urls import path

urlpatterns = [
    path('tracking/', tracking_view, name="tracking"),
    path('noOrder/', no_order_view, name="no-order"),
    path('orderHistory/', orderhistory_view, name="order-history"),
    path('order/', place_order_view, name="order"),
    path('add-to-order/<int:pk>/', add_to_order, name="add-to-order"),
]
