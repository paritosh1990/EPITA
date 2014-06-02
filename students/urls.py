from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
   #URLs used when not signed in (views and functionality stored in root app).
   # They are accessed here, to make the URL prettier
   url(r'^$', views.StudentProfileView.as_view(), name='profile'),
   url(r'^sign_up/$', views.SignUpView.as_view(), name='sign_up'),
)