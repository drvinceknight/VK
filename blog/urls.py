from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<slug>[\w\-]+)/$', views.post),
)
