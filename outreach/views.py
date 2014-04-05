from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course
from research.models import Paper
from homepage.views import Commit
from news.views import Item
from outreach.models import Activity
from markdown import markdown

def index(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    activities = Activity.objects.all()

    context = {'latest_video_list': latest_video_list,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,
               'news': news,
               'latest_paper_list': latest_paper_list,
               'activities': activities,
               }

    return render_to_response('outreach/index.html', context)

def activity(request, slug):
    activity = get_object_or_404(Activity, slug=slug)
    activity.content = markdown(activity.content)
    context = {'activity' : activity}

    return render(request, 'outreach/activity.html', context)
