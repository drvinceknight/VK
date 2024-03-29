from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<paper_id>\d+)/$', views.detail, name='detail'),
    url(r'^publicationlist.html$', views.publicationlist, name='publicationlist'),
    url(r'^projects/(?P<project_id>\d+)/$', views.projectdetail, name='projectdetail'),
    url(r'^projects/$', views.projectlist, name='projectlist'),
    url(r'^researchstudents/(?P<student_id>[\w\-]+)/$', views.researchstudent),
    url(r'^researchstudents/$', views.researchstudentindex),
    url(r'^researchstudents/list/(?P<category>[\w\-]+)/$', views.categorylist),
)
