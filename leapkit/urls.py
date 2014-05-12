from django.conf.urls import patterns, include, url

from root import views

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^home/', include('root.urls', namespace="root")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^companies/', include('companies.urls', namespace="companies")),
    url(r'^admin/', include('admin.urls', namespace="admin")),
)
