from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, GroupRequiredMixin


class StudentProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "student_profile.html"
    login_url = "sign_in"
    group_required = u"Students"


