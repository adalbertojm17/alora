from django.shortcuts import render, redirect
from .forms import FeedBackForm


def feedback_view(request):

    context = {}

    if request.POST:
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contconfirm')
        else:
            context['feedback_form'] = form
    else:
        form = FeedBackForm()
        context['feedback_form'] = form
    return render(request, 'contact.html', context)


def feedbackconfirm_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "contactconfirm.html", my_context)
