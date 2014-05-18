from django.shortcuts 			import get_object_or_404, render
from django.http 				import HttpResponseRedirect
from django.core.urlresolvers 	import reverse
from django.views 				import generic
from django.utils 				import timezone

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