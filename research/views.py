from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from git import Repo

from homepage.views import Commit
from research.models import Paper, Project

def index(request):
    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]

    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][::-1]
        latest_commits = latest_commits[:5]
    except:
        latest_commits = []


    context = {'latest_commits': latest_commits,
               'latest_paper_list': latest_paper_list}

    return render_to_response('research/index.html', context)


def detail(request, paper_id):

    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][::-1]
        latest_commits = latest_commits[:5]
    except:
        latest_commits = []

    paper = get_object_or_404(Paper, pk=paper_id)

    context = {'paper' : paper,
               'latest_commits' : latest_commits}
    return render(request, 'research/detail.html', context)

def publicationlist(request):
    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][::-1]
        latest_commits = latest_commits[:5]
    except:
        latest_commits = []

    paper_list = Paper.objects.all().order_by('-pub_date')

    context = {'paper_list' : paper_list,
               'latest_commits' : latest_commits}

    return render_to_response('research/publicationlist.html', context)

def projectdetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][::-1]
        latest_commits = latest_commits[:5]
    except:
        latest_commits = []

    context = {'project' : project,
               'latest_commits' : latest_commits}

    return render(request, 'research/projectdetail.html', context)

def projectlist(request):
    try:
        # Attempt to read log file: I'm not sure I'm happy with it being hard rooted...
        commitlog = open('/var/www/VK/static/commitlog', 'r')
        commits = commitlog.read()
        commits = commits.split('\n')
        commitlog.close()
        latest_commits = [c[c.index('commit') + len('commit: '):] for c in commits if 'commit: ' in c][::-1]
        latest_commits = latest_commits[:5]
    except:
        latest_commits = []

    current_project_list = [project for project in Project.objects.all() if not project.complete]

    context = {'current_project_list' : current_project_list,
               'latest_commits' : latest_commits}

    return render(request, 'research/projectlist.html', context)
