from django.conf.urls import patterns, url

from bills import views

urlpatterns = patterns(
    '',
    # ex: /bills/
    url(r'^$', views.index, name='index'),
    # ex: /bills/new/
    url(r'^new/$', views.new, name='new'),
    # ex: /bills/3/
    url(r'^(?P<bill_id>\d+)/$', views.detail, name='detail'),
    # ex: /bills/3/edit
    url(r'^(?P<bill_id>\d+)/edit/$', views.edit, name='edit'),
)