from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(' ',
    # Examples:
    # url(r'^blog/', include('blog.urls')),  
    url(r'^$', include('polls.urls')),  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'admin/', include(admin.site.urls))
)