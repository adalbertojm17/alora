from django.urls import path

from .views import (
    ServiceListAPIView,
    ServiceDetailAPIView,
    StoreListAPIView,
)

urlpatterns = [

    path('service-list', ServiceListAPIView.as_view(), name='api-service-list'),
    path('service-details/', ServiceDetailAPIView.as_view(), name='api-service-detail'),
    path('store-list/', StoreListAPIView.as_view(), name='api-service-detail'),
]
