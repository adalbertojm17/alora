from django.shortcuts import render, redirect
from .forms import FeedBackForm


def feedback_view(request):
    context = {}

    if request.POST:
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedBackForm()
            request.session['form-submitted'] = True
            return redirect('contact-confirm')
        else:
            context['feedback_form'] = form
    else:
        form = FeedBackForm()
        context['feedback_form'] = form
    return render(request, 'contact.html', context)


def feedbackconfirm_view(request, *args, **kwargs):
    if not request.session.get('form-submitted', False):
        return redirect('contact')
    request.session['form-submitted'] = False
    return render(request, "contactconfirm.html")
