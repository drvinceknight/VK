from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from git import Repo

from homepage.views import Commit
from research.models import Paper, Project

def index(request):
    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]

    context = {'latest_paper_list': latest_paper_list}

    return render_to_response('research/index.html', context)


def detail(request, paper_id):

    paper = get_object_or_404(Paper, pk=paper_id)

    context = {'paper' : paper}

    return render(request, 'research/detail.html', context)

def publicationlist(request):

    paper_list = Paper.objects.all().order_by('-pub_date')

    context = {'paper_list' : paper_list}


    return render_to_response('research/publicationlist.html', context)

def projectdetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    context = {'project' : project}

    return render(request, 'research/projectdetail.html', context)

def projectlist(request):
    current_project_list = [project for project in Project.objects.all() if not project.complete]

    context = {'current_project_list' : current_project_list}


    return render(request, 'research/projectlist.html', context)
