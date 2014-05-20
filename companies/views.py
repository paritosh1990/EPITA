from django.shortcuts 			import render
from django.views 				import generic

# Create your views here.
class CompanyProfileView(generic.TemplateView):
	template_name = "company_profile.html"