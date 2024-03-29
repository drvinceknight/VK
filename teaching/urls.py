from django.conf.urls import patterns, url

from teaching import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^computingformathematics.html$', views.computingformathematics),
    url(r'^PCUTL$', views.pcutl),
    url(r'^fairmarks/$', views.fairmarks),
    url(r'^(?P<slug>[\w\-]+)/$', views.courseindex),
    url(r'^(?P<slug>[\w\-]+)/readinglist/$', views.readinglist),
    url(r'^(?P<courseslug>[\w\-]+)/homework/(?P<slug>[\w\-]+)$', views.homework),
    url(r'^(?P<courseslug>[\w\-]+)/homework/solution/(?P<slug>[\w\-]+)$', views.solution),
    url(r'^(?P<courseslug>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.coursecontent),
    url(r'^(?P<courseslug>[\w\-]+)/alternative/(?P<slug>[\w\-]+)/$', views.alternativecontent),
    url(r'^(?P<courseslug>[\w\-]+)/assessment/(?P<slug>[\w\-]+)/$', views.assessment),
    )
