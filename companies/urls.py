from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
   url(r'^$', views.CompanyProfileView.as_view(), name='profile'),
   url(r'^sign_up$', views.SignUpView.as_view(), name='sign_up'),
)