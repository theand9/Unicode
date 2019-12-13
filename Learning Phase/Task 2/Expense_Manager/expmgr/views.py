from . import models, forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from django.template import loader
from django.forms import modelformset_factory


# Create your views here.
def MainLoginView(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)

        if form.is_valid():
            submit_Form = form.save(commit=False)
            if models.loginDetails.objects.filter(SAP_ID=form.cleaned_data.get("SAP_ID")).exists():
                return redirect('welcomescreen/')

    else:
        form_Render = forms.UserLoginForm

    return render(request, 'login.html', {'form': form_Render})


def MainSignupView(request):
    if request.method == 'POST':
        form = forms.UserSignupForm(request.POST)

        if form1.is_valid():
            submit_Form = form.save()

    else:
        form_Render1 = forms.UserSignupForm

    return render(request, 'signup.html', {'form1': form_Render1})
