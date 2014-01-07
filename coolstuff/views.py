from django.shortcuts import render
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from coolstuff.models import UsefullLink
import time

from random import sample

from homepage.views import Commit

def index(request):
    numberoflinks = 5
    link_selection = sample(UsefullLink.objects.all(), numberoflinks)

    context = {'link_selection': link_selection}

    return render_to_response('coolstuff/index.html', context)

def usefullinks(request):
    links = UsefullLink.objects.all().order_by("title")


    context = {'links': links}


    return render_to_response('coolstuff/usefullinks.html', context)

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
