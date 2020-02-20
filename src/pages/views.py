from django.shortcuts import render


def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "index.html", my_context)


def main_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "mainpage.html", my_context)

def aboutus_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "aboutus.html", my_context)

def contactus_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "contactus.html", my_context)
