from django.conf.urls import patterns, include, url
from django.contrib import admin

from root import views

admin.autodiscover()

urlpatterns = patterns('',

	#URLs used when not signed in (views and functionality stored in root app). They are accessed here, to make the URL prettier
    url(r'^$', views.HomepageView.as_view(), name='home'),
   	url(r'student-info/$', views.StudentInfoView.as_view(), name='student_info'),
    url(r'company-info/$', views.CompanyInfoView.as_view(), name='company_info'),
    url(r'university-info/$', views.UniversityInfoView.as_view(), name='university_info'),
    url(r'get-started/$', views.GetStartedView.as_view(), name='getting_started'),
    url(r'about-leapkit/$', views.AboutLeapkitView.as_view(), name='about_leapkit'),
    url(r'FAQ/$', views.FAQView.as_view(), name='FAQ'),
    url(r'contact-leapkit/$', views.ContactLeapView.as_view(), name='contact_leapkit'),
    url(r'signin/$', views.SignInView.as_view(), name='sign_in'),
    url(r'student_signup/$', views.StudentSignUpView.as_view(), name='student_sign_up'),
    url(r'company_signup/$', views.CompanySignUpView.as_view(), name='company_sign_up'),
    url(r'signup/$', views.SignUpView.as_view(), name='sign_up'),

    #All other URLs are stored in their respective app.
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^companies/', include('companies.urls', namespace="companies")),
    url(r'^admin/', include(admin.site.urls)),
)
