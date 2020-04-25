from django.urls import path

from .views import (
    PlaceOrderAPIView,
    DisplayOrderAPIView,
    RegionListAPIView,
    ItemListAPIView
)

urlpatterns = [
    path('place-order/', PlaceOrderAPIView.as_view(), name='api-place-order'),
    path('order-details/', DisplayOrderAPIView.as_view(), name='api-order-details'),
    path('item-list/', ItemListAPIView.as_view(), name='api-item-details'),
    path('region-list/', RegionListAPIView.as_view(), name='api-region-list'),
]
