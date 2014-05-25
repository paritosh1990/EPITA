from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, GroupRequiredMixin


class StudentProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    permission_required = "auth.change_user"
    template_name = "student_profile.html"
    group_required = u"students"
    login_url = "/signin/"