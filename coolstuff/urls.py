from django.conf.urls import patterns, url

from coolstuff import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^randomplot.png$', views.randomplot),
    url(r'^usefullinks.html$', views.usefullinks),
    url(r'^lettersofrecommendation$', views.lettersofrecommendation),
    url(r'^lettersofrecommendation/(?P<letter_id>\d+)/$', views.letter, name='letter'),
    url(r'^pcs/(?P<name>[\w\-]+)/$', views.pc),
    url(r'^error$', views.error),
    )
