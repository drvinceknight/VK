from django.conf.urls import patterns, url

from coolstuff import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    )
