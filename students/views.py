from django.views.generic import TemplateView, FormView

from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .forms import StudentCreationForm


class StudentProfileView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "student_profile.html"
    login_url = "students:sign_up"
    group_required = u"Students"


class SignUpView(FormView):
    template_name = "student_signup.html"
    form_class = StudentCreationForm
    success_url = "students:profile"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(SignUpView, self).form_valid(form)