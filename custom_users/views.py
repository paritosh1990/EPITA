from django.contrib import auth
from django.http import HttpResponseRedirect

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

        if user.user_type == "STU":
            return HttpResponseRedirect('/students/')
        elif user.user_type == "COM":
            return HttpResponseRedirect('/companies/')
        else:
            return HttpResponseRedirect('/admin/')
    else:
        return HttpResponseRedirect('leapkit:home')