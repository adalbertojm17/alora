from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    UserCreateAPIView,
    UserListAPIView,
    UserLoginAPIView,
    # UserUpdateAPIView,
)

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('get-user-auth-token/', obtain_auth_token, name='get_user_auth_token'),
    path('login/', UserLoginAPIView.as_view(), name='api-login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    # path('update/', UserUpdateAPIView.as_view(), name='update'),
]
