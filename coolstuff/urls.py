from django.conf.urls import patterns, url

from coolstuff import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^randomplot.png$', views.randomplot),
    url(r'^error$', views.error),
    )
