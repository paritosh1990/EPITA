from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, GroupRequiredMixin


class CompanyProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    permission_required = "auth.change_user"
    template_name = "company_profile.html"
    group_required = u"companies"
    login_url = "/signin/"