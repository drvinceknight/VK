from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from git import Repo

from homepage.views import commitdate
from research.models import Paper

def detail(request, paper_id):

    latest_commits = ["%s: %s" % (commitdate(c), c.message) for c in Repo("./").iter_commits('Head', max_count=5)]

    paper = get_object_or_404(Paper, pk=paper_id)

    context = {'paper' : paper,
               'latest_commits' : latest_commits}
    return render(request, 'research/detail.html', context)

