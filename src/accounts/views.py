from django.contrib.auth import login, logout
from .backends import authenticate
from django.shortcuts import render, redirect

from .forms import RegistrationForm, AccountAuthenticationForm, EditAccountForm
from .models import Account


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account, backend='accounts.backends.EmailOrUsernameModelBackend')

            return redirect('main')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_manager:
            return redirect('staffhome')
        return redirect('main')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user, backend='accounts.backends.EmailOrUsernameModelBackend')
                if user.is_manager:
                    return redirect('staffhome')
                return redirect('main')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def edit_account_view(request):
    obj = Account.objects.get(id=request.user.id)
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        'phone': obj.phone,
        'user': request.user,
    }
    if request.POST:
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = EditAccountForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "phone": context['phone'],
                "email": request.user.email,
                "email2": request.user.email,
                "username": request.user.username,
            }
        )
    context["account_form"] = form
    return render(request, "edit_account_page.html", context)
