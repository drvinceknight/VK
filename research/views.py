from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from git import Repo

from homepage.views import Commit
from research.models import Paper

def index(request):
    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]

    latest_commits = [Commit(c)  for c in Repo("./").iter_commits('Head', max_count=5)]


    context = {'latest_commits': latest_commits,
               'latest_paper_list': latest_paper_list}

    return render_to_response('research/index.html', context)


def detail(request, paper_id):

    latest_commits = [Commit(c)  for c in Repo("./").iter_commits('Head', max_count=5)]

    paper = get_object_or_404(Paper, pk=paper_id)

    context = {'paper' : paper,
               'latest_commits' : latest_commits}
    return render(request, 'research/detail.html', context)

