from django.conf.urls import patterns, url

from teaching import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^computingformathematics.html$', views.computingformathematics),
    )
