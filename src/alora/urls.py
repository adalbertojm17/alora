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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import (
    home_view,
    main_view,
    aboutus_view,
    contactus_view,
    services_view,
    order_view,
    orderconfirm_view,
    orderdestination_view,
    vieworder_view,
    orderhistory_view
)
from accounts.views import (
    registration_view,
    login_view,
    logout_view,
    edit_account_view
)

urlpatterns = [
    path('signup/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', home_view, name="home"),
    path('main/', main_view, name="main"),
    path('aboutus/', aboutus_view, name="aboutus"),
    path('contactus/', contactus_view, name="contactus"),
    path('edit_account/', edit_account_view, name="editaccount"),
    path('services/', services_view, name="services"),
    path('order/', order_view, name="Order"),
    path('orderconfirm/', orderconfirm_view, name="orderconfirm"),
    path('orderdestination/', orderdestination_view, name="orderdestination"),
    path('vieworder/', vieworder_view, name="vieworder"),
    path('orderhistory/', orderhistory_view, name="orderhistory"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
