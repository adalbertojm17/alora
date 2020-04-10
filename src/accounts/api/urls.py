from django.urls import path

from .views import (
    MyAuthToken,
    UserCreateAPIView,
    UserListAPIView,
    UserProfileAPIView,
    UserLogoutAPIView)

urlpatterns = [
    path('', UserListAPIView.as_view(), name='api-user-list'),
    path('get-user-auth-token/', MyAuthToken.as_view(), name='get_user_auth_token'),
    path('logout/', UserLogoutAPIView.as_view(), name='api-logout'),
    path('register/', UserCreateAPIView.as_view(), name='api-register'),
    path('profile/', UserProfileAPIView.as_view(), name='api-profile'),
]
