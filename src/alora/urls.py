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
# noinspection PyPackageRequirements,PyUnresolvedReferences
from feedback.views import (
    feedbackconfirm_view,
    feedback_view,
)
# noinspection PyUnresolvedReferences
from pages.views import (
    home_view,
    main_view,
    about_view,
    services_view
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    path('', home_view, name="home"),
    path('main/', main_view, name="main"),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include('accounts.api.urls'), name='users-api'),
    path('', include('accounts.urls'), name='accounts'),
    path('', include('business.urls'), name='business'),
    path('aboutus/', about_view, name="about"),
    path('contactus/', feedback_view, name="contact"),
    path('contactconfirm/', feedbackconfirm_view, name="contconfirm"),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
