from django.views.generic import TemplateView, FormView

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .forms import CompanyCreationForm


class CompanyProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "company_profile.html"
    group_required = u"Companies"
    login_url = "companies:sign_up"


class SignUpView(FormView):
    template_name = "company_signup.html"
    form_class = CompanyCreationForm
    success_url = "companies:profile"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(SignUpView, self).form_valid(form)