from django.shortcuts 			import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.views 				import generic


from .models import Question

class HomepageView(generic.TemplateView):
	template_name = "index.html"

class StudentInfoView(generic.TemplateView):
	template_name = "students.html"

class CompanyInfoView(generic.TemplateView):
	template_name = "companies.html"

class UniversityInfoView(generic.TemplateView):
	template_name = "universities.html"

class GetStartedView(generic.TemplateView):
	template_name = "get_started.html"

class AboutLeapkitView(generic.TemplateView):
	template_name = "about.html"

class FAQView(generic.ListView):
	model = Question
	template_name = "FAQ.html"

class ContactLeapView(generic.TemplateView):
	template_name = "contact.html"

class SignInView(generic.TemplateView):
	template_name = "signin.html"

class SignUpView(generic.TemplateView):
	template_name = "signup.html"