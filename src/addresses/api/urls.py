from django.urls import path

from .views import AddressAPIView, CreateAddressAPIView

urlpatterns = [
    path('address/', AddressAPIView.as_view(), name='address'),
    path('address/create/', CreateAddressAPIView.as_view(), name='create-address'),
]
