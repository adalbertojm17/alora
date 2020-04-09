from django.urls import path

from .views import (
    CreateOrderAPIView,
    DisplayOrderAPIView,
)

urlpatterns = [
    path('create', CreateOrderAPIView.as_view(), name='api-place-order'),
    path('details/', DisplayOrderAPIView.as_view(), name='api-order-details'),
]
