from django.shortcuts import render


def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "mainpage.html", my_context)
