from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', include('root.urls', namespace="root")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^companies/', include('companies.urls', namespace="companies")),
    url(r'^admin/', include('admin.urls', namespace="admin")),
)
