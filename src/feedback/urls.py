from django.urls import path

from .views import (
    feedback_view,
    feedbackconfirm_view
)

urlpatterns = [
    path('contact-us/', feedback_view, name="contact"),
    path('contact-confirm/', feedbackconfirm_view, name="cont-confirm"),

]
