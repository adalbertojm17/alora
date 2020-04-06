from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    MyAuthToken,
    UserCreateAPIView,
    UserListAPIView,
    UserLoginAPIView,
    UserProfileAPIView,
)

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('get-user-auth-token/', MyAuthToken.as_view(), name='get_user_auth_token'),
    path('login/', UserLoginAPIView.as_view(), name='api-login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]
