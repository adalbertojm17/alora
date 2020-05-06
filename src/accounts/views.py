# noinspection PyUnresolvedReferences
import time

from addresses.models import Address
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from formtools.wizard.views import SessionWizardView

from .backends import authenticate
from .forms import EditAddressForm, UserSignUpForm, UserAddressForm, AccountAuthenticationForm, AccountForm
from .models import Account
from .tokens import account_activation_token


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
        user.is_active = False

        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form_dict.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(template_name='registration/email_verification_done.html', request=self.request)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request=request, template_name='registration/email_verification_complete.html')
    else:
        return HttpResponse('Activation link is invalid!')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_manager or user.is_employee:
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
                if user.is_manager or user.is_employee:
                    return redirect('staffhome')
                return redirect('main')

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
    context = {}

    if request.POST:
        form = EditAddressForm(request.POST, instance=request.user.address)
        if form.is_valid():
            form.save()


    else:
        form = EditAddressForm(instance=request.user.address)

    context["Edit_Address_form"] = form
    return render(request, "edit_address.html", context)


def delete_account_view(request):
    return render(request, 'Confirm_account_cancelation.html')


def delete_account_function(request):
    object = request.user
    object.delete()
    return HttpResponseRedirect('/home/')
