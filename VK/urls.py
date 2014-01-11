from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('homepage.urls', namespace='homepage')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^research/', include('research.urls', namespace='research')),
    url(r'^teaching/', include('teaching.urls', namespace='teaching')),
    url(r'^outreach/', include('outreach.urls', namespace='outreach')),
    url(r'^coolstuff/', include('coolstuff.urls', namespace='coolstuff')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^unpeudemath/', include('blog.urls', namespace='blog')),
)
