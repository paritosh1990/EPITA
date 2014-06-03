from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from root import views
import leapkit_users.views as user_view

admin.autodiscover()

urlpatterns = patterns('',
   #URLs used when not signed in (views and functionality stored in root app).
   # They are accessed here, to make the URL prettier

   #Basic navigation urls
   url(r'^$', views.HomepageView.as_view(), name='home'),
   url(r'student-info/$', views.StudentInfoView.as_view(), name='student_info'),
   url(r'company-info/$', views.CompanyInfoView.as_view(), name='company_info'),
   url(r'university-info/$', views.UniversityInfoView.as_view(), name='university_info'),
   url(r'get-started/$', views.GetStartedView.as_view(), name='getting_started'),
   url(r'about-leapkit/$', views.AboutLeapkitView.as_view(), name='about_leapkit'),
   url(r'FAQ/$', views.FAQView.as_view(), name='FAQ'),

   # All urls related to contacting leapkit
   url(r'contact-leapkit/$', views.ContactLeapkitView.as_view(), name='contact_leapkit'),
   url(r'contact-leapkit/success/$', views.ContactSuccessView.as_view(), name='contact_success'),

   # Urls related to signing in/up
   url(r'sign_in/$', user_view.SignInView.as_view(), name='sign_in'),
   url(r'auth_view/$', user_view.auth_view, name='auth_view'),
   url(r'signup/$', views.SignUpView.as_view(), name='sign_up'),

   # All other URLs are stored in their respective app.
   url(r'^students/', include('students.urls', namespace="students")),
   url(r'^companies/', include('companies.urls', namespace="companies")),
   url(r'^admin/', include(admin.site.urls)),
) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
