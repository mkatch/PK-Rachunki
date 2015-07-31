from django.conf.urls import patterns, url

from bills import views
from bills import forms
from bills import api

urlpatterns = patterns(
    '',
    # ex: /bills/
    url(r'^$', views.index, name='index'),
    # ex: /bills/new/
    url(r'^new/$', views.new, name='new'),
    # ex: /bills/3/
    url(r'^(?P<bill_id>\d+)/$', views.detail, name='detail'),
    # ex: /bills/3/edit
    url(r'^(?P<bill_id>\d+)/edit/$', forms.edit_bill, name='edit'),

    # ex: /bills/api/clients/
    url(r'^api/clients/$', api.clients),
)