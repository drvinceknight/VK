from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<paper_id>\d+)/$', views.detail, name='detail'),
    url(r'^publicationlist$', views.publicationlist, name='publicationlist'),
)
