from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

from .forms import ContactForm

from .models import Question


class HomepageView(TemplateView):
    template_name = "index.html"


class StudentInfoView(TemplateView):
    template_name = "students.html"


class CompanyInfoView(TemplateView):
    template_name = "companies.html"


class UniversityInfoView(TemplateView):
    template_name = "universities.html"


class GetStartedView(TemplateView):
    template_name = "get_started.html"


class AboutLeapkitView(TemplateView):
    template_name = "about.html"


class FAQView(ListView):
    model = Question
    template_name = "FAQ.html"


class ContactLeapkitView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "success"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ContactLeapkitView, self).form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = "contact_success.html"


class SignUpView(TemplateView):
    template_name = "signup.html"

