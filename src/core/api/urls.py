from django.urls import path

from .views import (
    CreateOrderAPIView,
    DisplayOrderAPIView,
)

urlpatterns = [
    path('place-order', CreateOrderAPIView.as_view(), name='api-place-order'),
    path('order-details/', DisplayOrderAPIView.as_view(), name='api-order-details'),
]
