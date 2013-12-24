from django.shortcuts import render
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from vids.models import Video

def index(request):
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_commits = [c.message for c in Repo("./").iter_commits('Head', max_count=5)]


    context = {'latest_video_list': latest_video_list, 'latest_commits': latest_commits}
    return render_to_response('homepage/index.html', context)
