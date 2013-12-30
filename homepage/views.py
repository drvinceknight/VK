from django.shortcuts import render
from django.shortcuts import render_to_response
#from git import Repo This library does not seem to work...
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course
from research.models import Paper
import time

class Commit():
    """
    Class to take commit from pythongit and create own commit
    """
    def __init__(self, c):
        self.message = c.message
        self.date = time.strftime("%Y-%m-%d-%H-%M",time.gmtime(c.committed_date))

def index(request):
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:5]

    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][:5]
    except:
        latest_commits = []

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'latest_video_list': latest_video_list,
               'latest_commits': latest_commits,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,
               'latest_paper_list': latest_paper_list}

    return render_to_response('homepage/index.html', context)
