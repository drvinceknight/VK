from django.conf.urls import patterns, url

from outreach import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'(?P<slug>[\w\-]+)/$', views.activity),
    )
