from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .forms import StudentCreationForm
from .models import StudentProfile


class StudentProfileView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    template_name = "student_profile.html"
    login_url = "students:sign_up"
    group_required = u"Students"
    model = StudentProfile


class SignUpView(CreateView):
    template_name = "student_signup.html"
    form_class = StudentCreationForm

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['email'],
                            password=self.request.POST['password1'])
        if user is not None:
            login(self.request, user)
            self.success_url = user.get_absolute_url()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect("students:sign_up")


