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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

from pages.views import (
    home_view,
    main_view,
    about_view,
    services_view,
    no_order_view
)
from accounts.views import (
    registration_view,
    login_view,
    logout_view,
    edit_account_view,
)

from feedback.views import (
    feedbackconfirm_view,
    feedback_view,
)

from business.views import (
    staffhome_view,
    current_orders_view,
    general_info_view,
    staff_view,
    store_orderhistory_view
)

from orders.views import (
    order_view,
    orderconfirm_view,
    orderdestination_view,
    vieworder_view,
    orderhistory_view,
    load_service_view
)



urlpatterns = [
    path('signup/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', home_view, name="home"),
    path('main/', main_view, name="main"),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include('accounts.api.urls'), name='users-api'),
    path('aboutus/', about_view, name="about"),
    path('contactus/', feedback_view, name="contact"),
    path('contactconfirm/', feedbackconfirm_view, name="contconfirm"),
    path('edit_account/', edit_account_view, name="editaccount"),
    path('services/', services_view, name="services"),
    path('order/', order_view, name="order"),
    path('orderconfirm/', orderconfirm_view, name="orderconfirm"),
    path('orderdestination/', orderdestination_view, name="orderdestination"),
    path('vieworder/', vieworder_view, name="vieworder"),
    path('orderhistory/', orderhistory_view, name="orderhistory"),
    path('noorder/', no_order_view, name="noorder"),
    path('home/', staffhome_view, name="staffhome"),
    path('currentorders/', current_orders_view, name="currentorders"),
    path('generalinfo/', general_info_view, name="generalinfo"),
    path('staff/', staff_view, name="staff"),
    path('storeorders/', store_orderhistory_view, name="storeorders"),
    path('admin/', admin.site.urls),
    path('ajax/load-names/',load_service_view , name='ajax_load_names'),


    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]

urlpatterns += staticfiles_urlpatterns()
