# noinspection PyUnresolvedReferences
import time

from django.http import HttpResponseRedirect

from .forms import EditAddressForm
from addresses.models import Address
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView

from .backends import authenticate
from .forms import UserSignUpForm, UserAddressForm, AccountAuthenticationForm, AccountForm
from .models import Account


class RegistrationView(SessionWizardView):
    template_name = "signup.html"
    form_list = [UserSignUpForm, UserAddressForm]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_manager:
                return redirect('staffhome')
            return redirect('main')
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        form_dict = self.get_all_cleaned_data()
        first_name = form_dict.get('first_name')
        last_name = form_dict.get('last_name')
        email = form_dict.get('email')
        phone = form_dict.get('phone')
        username = form_dict.get('username')
        raw_password = form_dict.get('password1')
        street = form_dict.get('street')
        apt = form_dict.get('apt')
        city = form_dict.get('city')
        state = form_dict.get('state')
        zip_code = form_dict.get('zip_code')
        address, created = Address.objects.get_or_create(
            street=street,
            apt=apt,
            city=city,
            state=state,
            zip_code=zip_code
        )

        user = Account.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            username=username,
            address=address,
        )
        user.set_password(raw_password=raw_password)
        user.save()
        account = authenticate(username=username, password=raw_password)
        login(self.request, account, backend='accounts.backends.EmailOrUsernameModelBackend')

        return redirect('main')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_manager:
            return redirect('staffhome')
        if user.is_employee:
            return redirect('staffhome')
        return redirect('main')

    if request.POST:
        form = AccountAuthenticationForm(request.POST, current_login='customer-login')
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user, backend='accounts.backends.EmailOrUsernameModelBackend')
                if user.is_manager:
                    return redirect('staffhome')
                if user.is_staff:
                    return redirect('staffhome')
                return redirect('main')
        # else:
        #     if form.redirect:
        #         time.sleep(5)
        #         return redirect('businesslogin')

    else:
        form = AccountAuthenticationForm(current_login='customer-login')

    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def business_login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_manager:
            return redirect('staffhome')
        if user.is_employee:
            return redirect('currentorders')

    if request.POST:
        form = AccountAuthenticationForm(request.POST, current_login='business-login')
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user, backend='accounts.backends.EmailOrUsernameModelBackend')
                if user.is_manager:
                    return redirect('staffhome')
                if user.is_employee:
                    return redirect('currentorders')

    else:
        form = AccountAuthenticationForm(current_login='business-login')

    context['login_form'] = form
    return render(request, 'business/business_login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    obj = Account.objects.get(id=request.user.id)
    context = {
        'phone': obj.phone,
        'user': request.user,
    }
    if request.POST:
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = AccountForm(
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
    return render(request, "account_page.html", context)

def edit_address_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context= {}

    if request.POST:
        form = EditAddressForm(request.POST, instance=request.user.address)
        if form.is_valid():
            form.save()


    else:
        form =EditAddressForm(instance=request.user.address)

    context["Edit_Address_form"] = form
    return render(request, "edit_address.html", context)

def delete_account_view(request):
    return render(request,'Confirm_account_cancelation.html')

def delete_account_function(request):
    object = request.user
    object.delete()
    return HttpResponseRedirect('/home/')