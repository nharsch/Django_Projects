from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views #not sure if this is the best way

admin.autodiscover()

urlpatterns = patterns('',
	#this is a tuple

	#it must be named urlpatterns

    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
	#this maps empty strings to index

    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^rango/', include('rango.urls'))
)
