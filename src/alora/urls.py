"""alora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include


urlpatterns = [
    path('', include('accounts.urls'), name='users'),
    path('', include('business.urls'), name='business'),
    path('', include('core.urls'), name='core'),
    path('', include('feedback.urls'), name='feedback'),
    path('', include('pages.urls'), name='pages'),
    path('api/users/', include('addresses.api.urls'), name='addresses-api'),
    path('api/users/', include('accounts.api.urls'), name='users-api'),
    path('api/business/', include('business.api.urls'), name='business'),
    path('api/core/', include('core.api.urls'), name='core'),
    path('api/', include('feedback.api.urls'), name='feedback'),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
