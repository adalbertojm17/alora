from django.shortcuts import render, redirect
from django.http import Http404


def staffhome_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_manager:
        raise Http404
    return render(request, "business/home.html", my_context)


def current_orders_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_manager:
        raise Http404
    return render(request, "business/current_orders.html", my_context)


def general_info_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_manager:
        raise Http404
    return render(request, "business/general_info.html", my_context)


def staff_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_manager:
        raise Http404
    return render(request, "business/staff.html", my_context)


def store_orderhistory_view(request, *args, **kwargs):
    my_context = {}
    if not request.user.is_manager:
        raise Http404
    return render(request, "business/store_orderhistory.html", my_context)
