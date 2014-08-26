from django.conf.urls import patterns, include, url
# from main import views

urlpatterns = patterns('', 
	url(r'^$', 'main.views.home', name='home'),
    url(r'^(?P<batch_id>\d+)/$', 'main.views.batchview', name='batchview'),                       
    url(r'^(?P<batch_id>\d+)/batchview/$', 'main.views.batchview', name='batchview'),
)