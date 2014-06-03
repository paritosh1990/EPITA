from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, FormView, CreateView

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .forms import CompanyCreationForm


class CompanyProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "company_profile.html"
    group_required = u"Companies"
    login_url = "companies:sign_up"


class SignUpView(CreateView):
    template_name = "company_signup.html"
    form_class = CompanyCreationForm
    success_url = "/companies/"

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['email'],
                            password=self.request.POST['password1'])
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)