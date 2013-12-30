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

    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]

    #latest_commits = [Commit(c)  for c in Repo("./").iter_commits('Head', max_count=5)]
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

    return render_to_response('coolstuff/index.html', context)

def randomplot(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def error(request):
    import django
    return django.http.HttpResponse('Error %s' % vince)
