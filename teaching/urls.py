from django.conf.urls import patterns, url

from teaching import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^computingformathematics.html$', views.computingformathematics),
    url(r'^PCUTL$', views.pcutl),
    url(r'^(?P<slug>[\w\-]+)/$', views.courseindex),
    url(r'^(?P<slug>[\w\-]+)/readinglist/$', views.readinglist),
    url(r'^(?P<courseslug>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.coursecontent),
    )
