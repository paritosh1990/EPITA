from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from students import views 

urlpatterns = patterns('',
    
	#URLs used when not signed in (views and functionality stored in root app). They are accessed here, to make the URL prettier
    url(r'^$', views.StudentProfileView.as_view(), name='profile'),
 )