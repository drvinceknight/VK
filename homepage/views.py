from django.shortcuts import render
from django.shortcuts import render_to_response
#from git import Repo This library does not seem to work...
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course
from research.models import Paper, Project
from news.models import Item
import time

class Commit():
    """
    Class to take commit from pythongit and create own commit
    """
    def __init__(self, c):
        self.message = c.message
        self.date = time.strftime("%Y-%m-%d-%H-%M",time.gmtime(c.committed_date))

def index(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]

    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:5]
    current_project_list = [project for project in Project.objects.all() if not project.complete]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'latest_video_list': latest_video_list,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,
               'current_project_list': current_project_list,
               'latest_paper_list': latest_paper_list,
               'news': news,
               }

    return render_to_response('homepage/index.html', context)
