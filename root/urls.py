from django.conf.urls import patterns, include, url

from root import views

urlpatterns = patterns('',
    url(r'student/$', views.StudentInfoView.as_view(), name='student'),
    url(r'company/$', views.CompanyInfoView.as_view(), name='company'),
    url(r'university/$', views.UniversityInfoView.as_view(), name='university'),
    url(r'start/$', views.GetStartedView.as_view(), name='start'),
    url(r'about/$', views.AboutLeapkitView.as_view(), name='about'),
    url(r'FAQ/$', views.FAQView.as_view(), name='FAQ'),
    url(r'contact/$', views.ContactLeapView.as_view(), name='contact'),

)
