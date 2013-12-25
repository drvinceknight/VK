from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^(?P<paper_id>\d+)/$', views.detail),
)
