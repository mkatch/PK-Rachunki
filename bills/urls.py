from django.conf.urls import patterns, url

from bills import views

urlpatterns = patterns('',
    # ex: /bills/
    url(r'^$', views.index, name='index'),
    # ex: /bills/3/2014/
    url(r'^(?P<bill_id>\d+/\d+)/$', views.detail, name='detail')
)