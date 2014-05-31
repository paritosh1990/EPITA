from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import FormView

from students.forms import StudentCreationForm
from companies.forms import CompanyCreationForm

from .models import Question
from .forms import ContactForm, SignInForm


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


class SignInView(FormView):
    template_name = "signin.html"
    form_class = SignInForm


class CompanySignUpView(FormView):
    template_name = "company_signup.html"
    form_class = CompanyCreationForm
    success_url = "companies:profile"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(CompanySignUpView, self).form_valid(form)


class StudentSignUpView(FormView):
    template_name = "student_signup.html"
    form_class = StudentCreationForm
    success_url = "students:profile"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(StudentSignUpView, self).form_valid(form)


class SignUpView(TemplateView):
    template_name = "signup.html"


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)

        #Check to see if user is a student, if so, go to student profile page
        is_student = user.groups.all().filter(name="Students")
        if is_student:
            return HttpResponseRedirect('/students/')

        #Check to see if user is a company, if so, go to company profile page
        is_company = user.groups.all().filter(name="Companies")
        if is_company:
            return HttpResponseRedirect('/companies/')

        return HttpResponseRedirect('/about/')
    else:
        return HttpResponseRedirect('leapkit:home')
