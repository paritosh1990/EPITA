from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
   #URLs used when not signed in (views and functionality stored in root app).
   # They are accessed here, to make the URL prettier
   url(r'^$', views.StudentProfileView.as_view(), name='profile'),
   url(r'^login/$', views.login, name="login"),
   url(r'^auth/$', views.auth_view, name="authentication"),
   url(r'^logout/$', views.logout, name="logout"),
   url(r'^loggedin/$', views.loggedin, name="loggedin"),
   url(r'^invalid/$', views.invalid_login, name="invalid_login"),

)