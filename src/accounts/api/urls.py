from django.urls import path

from .views import (
    ObtainUserAuthToken,
    ValidateToken,
    UserCreateAPIView,
    UserListAPIView,
    UserProfileAPIView,
    UserLogoutAPIView,
    ChangePasswordAPIView
)


urlpatterns = [
    path('', UserListAPIView.as_view(), name='api-user-list'),
    path('get-user-auth-token/', ObtainUserAuthToken.as_view(), name='get_user_auth_token'),
    path('validate-auth-token/', ValidateToken.as_view(), name='validate_auth_token'),
    path('logout/', UserLogoutAPIView.as_view(), name='api-logout'),
    path('register/', UserCreateAPIView.as_view(), name='api-register'),
    path('profile/', UserProfileAPIView.as_view(), name='api-profile'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='api-password-change'),
]
