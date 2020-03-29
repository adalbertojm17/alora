from django.shortcuts import render, redirect


def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "index.html", my_context)


def main_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    my_context = {}
    return render(request, "mainpage.html", my_context)


def about_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "about.html", my_context)


def services_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "services.html", my_context)

def staffhome_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "home.html", my_context)