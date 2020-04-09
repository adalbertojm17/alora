from django.urls import path

from .views import (
    ServiceListAPIView,
    ServiceDetailAPIView,
)

urlpatterns = [
    path('list', ServiceListAPIView.as_view(), name='api-service-list'),
    path('details/', ServiceDetailAPIView.as_view(), name='api-service-detail'),
]
