from django.shortcuts import render
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course
from research.models import Paper
import time

from homepage.views import Commit

def index(request):
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_paper_list = Paper.objects.all().order_by('-publication_date')[:6]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'latest_video_list': latest_video_list,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,
               'latest_paper_list': latest_paper_list}

    return render_to_response('teaching/index.html', context)

def computingformathematics(request):

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,}


    return render_to_response('teaching/computingformathematics.html', context)
