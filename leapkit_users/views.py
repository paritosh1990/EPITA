from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from .forms import SignInForm


class SignInView(FormView):
    template_name = "signin.html"
    form_class = SignInForm


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)

        #Check to see if user is a student, if so, go to student profile page
        if user.user_type == "STU":
            return HttpResponseRedirect('/students/')

        #Check to see if user is a company, if so, go to company profile page
        if user.user_type == "COM":
            return HttpResponseRedirect('/companies/')

        #Check to see if user is staff, if so, go to the admin page
        if user.user_type == "STA":
            return HttpResponseRedirect('/admin/')

        return HttpResponseRedirect('404')
    else:
        return HttpResponseRedirect('leapkit:home')