from django.shortcuts import render
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course

def index(request):
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_commits = [c.message for c in Repo("./").iter_commits('Head', max_count=5)]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'latest_video_list': latest_video_list,
               'latest_commits': latest_commits,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list}

    return render_to_response('homepage/index.html', context)
