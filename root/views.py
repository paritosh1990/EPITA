from django.shortcuts 			import get_object_or_404, render
from django.http 				import HttpResponseRedirect
from django.core.urlresolvers 	import reverse
from django.views 				import generic
from django.utils 				import timezone
from django.views.generic import TemplateView

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

class FAQView(TemplateView):
	template_name = "FAQ.html"

class ContactLeapView(TemplateView):
	template_name = "contact.html"