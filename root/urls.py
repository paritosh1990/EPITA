from django.conf.urls import patterns, include, url

from root import views

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='index'),
)
