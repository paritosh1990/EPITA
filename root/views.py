from django.shortcuts 			import get_list_or_404, render
from django.contrib.auth 		import authenticate, login
from django.views.generic 		import TemplateView, ListView, CreateView


from .models import Question, UserQuery

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

class ContactLeapView(CreateView):
	model = UserQuery
	template_name = "contact.html"

	def form_valid(self, form):
		#Do custom logic

		return super(ContactLeapView, self).form_valid(form)

	def form_invalid(self, form):
		#Do custom logic

		return super(ContactLeapView, self).form_invalid(form)



class SignInView(TemplateView):
	template_name = "signin.html"

class CompanySignUpView(TemplateView):
	template_name = "company_signup.html"

class StudentSignUpView(TemplateView):
	template_name = "student_signup.html"

class SignUpView(TemplateView):
	template_name = "signup.html"