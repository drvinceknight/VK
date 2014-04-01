from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from git import Repo
import markdown

from homepage.views import Commit
from research.models import Paper, Project, Student
from news.models import Item

def index(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    latest_paper_list = Paper.objects.all().order_by('-pub_date')[:6]
    students = [student for student in Student.objects.all() if student.current()]

    context = {'latest_paper_list': latest_paper_list,
               'news':news,
               'students':students}

    return render_to_response('research/index.html', context)

def researchstudent(request, student_id):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]

    student = get_object_or_404(Student, pk=student_id)
    description = markdown.markdown(student.projectdescription, safe_made='escape')

    context = {'student' : student,
               'description' : description,
               'news' : news,}

    return render(request, 'research/researchstudent.html', context)

def detail(request, paper_id):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]

    paper = get_object_or_404(Paper, pk=paper_id)

    context = {'paper' : paper,
               'news' : news,}

    return render(request, 'research/detail.html', context)

def publicationlist(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]

    paper_list = Paper.objects.all().order_by('-pub_date')

    context = {'paper_list' : paper_list,
               'news': news}


    return render_to_response('research/publicationlist.html', context)

def projectdetail(request, project_id):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    project = get_object_or_404(Project, pk=project_id)

    context = {'project' : project,
               'news': news}

    return render(request, 'research/projectdetail.html', context)

def projectlist(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    current_project_list = [project for project in Project.objects.all() if not project.complete]

    context = {'current_project_list' : current_project_list,
               'news' : news}


    return render(request, 'research/projectlist.html', context)
