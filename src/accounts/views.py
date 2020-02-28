from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, EditAccountForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
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
        return redirect('main')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('main')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def edit_account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('main')

    else:
        form = EditAccountForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )
    context["account_form"] = form
    return render(request, "edit_account_page.html", context)
