from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class StudentProfileView(generic.TemplateView):
    template_name = "student_profile.html"