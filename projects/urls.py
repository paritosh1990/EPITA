from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.CreateProjectView.as_view(), name='profile'),
)