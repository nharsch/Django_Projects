from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Examples:
    # url(r'^$', 'CSVImport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls', namespace="main", app_name="main")),
    url(r'^$', include('main.urls', namespace="main", app_name="main")),                       
    # attempt to add views
    #  url(r'^BatchJob/', include('CSVImport'))
)
