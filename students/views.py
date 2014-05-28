from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from braces.views import LoginRequiredMixin, GroupRequiredMixin


class StudentProfileView(TemplateView):
    #permission_required = "auth.change_user"
    template_name = "student_profile.html"
    #group_required = u"students"
    #login_url = "/signin/"


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/students/loggedin/')
    else:
        return HttpResponseRedirect('/students/invalid/')


def logout(request):
    auth.logout(request)
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid.html')