from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, FormView, CreateView
from django.core.context_processors import csrf

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .forms import StudentCreationForm


class StudentProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "student_profile.html"
    login_url = "students:sign_up"
    group_required = u"Students"


class SignUpView(CreateView):
    template_name = "student_signup.html"
    form_class = StudentCreationForm
    success_url = "/students/"

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['email'],
                            password=self.request.POST['password1'])
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


