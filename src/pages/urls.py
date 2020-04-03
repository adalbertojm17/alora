# noinspection PyPackageRequirements,PyUnresolvedReferences
from django.urls import path

from .views import (
    home_view,
    main_view,
    about_view,
)

urlpatterns = [
    path('', home_view, name="home"),
    path('main/', main_view, name="main"),
    path('about-us/', about_view, name="about"),

]
