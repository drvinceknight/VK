from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from git import Repo
from urlparse import urlparse

from vids.models import Video
from teaching.models import Course, Content, ReadingListItem
from research.models import Paper
from news.models import Item
import time

from homepage.views import Commit

def index(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    latest_video_list = Video.objects.all().order_by('-pub_date')[:6]

    latest_paper_list = Paper.objects.all().order_by('-publication_date')[:6]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'latest_video_list': latest_video_list,
               'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'upcoming_course_list': upcoming_course_list,
               'news': news,
               'latest_paper_list': latest_paper_list}

    return render_to_response('teaching/index.html', context)

def courseindex(request, slug):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    course = get_object_or_404(Course, slug=slug)

    context = {'course': course,
               'news': news,}

    return render_to_response('teaching/courseindex.html', context)

def readinglist(request, slug):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    course = get_object_or_404(Course, slug='gametheory')
    readinglist = ReadingListItem.objects.filter(course=course).order_by('title')

    context = {'news':news,
               'course': course,
               'readinglist': readinglist,}
    return render_to_response('teaching/readinglist.html', context)


def coursecontent(request, courseslug, slug):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    course = get_object_or_404(Course, slug=courseslug)
    content = get_object_or_404(Content, course=course, slug=slug)

    nextcontent = Content.objects.filter(course=course).filter(id__gt=content.id).order_by('id')
    if len(nextcontent) > 0:
        nextcontent = nextcontent[0]
    else:
        nextcontent = False
    prevcontent = Content.objects.filter(course=course).filter(id__lt=content.id).order_by('-id')
    if len(prevcontent) > 0:
        prevcontent = prevcontent[0]
    else:
        prevcontent = False

    context = {'course': course,
               'content': content,
               'nextcontent': nextcontent,
               'prevcontent': prevcontent,
               'news': news,}


    return render_to_response('teaching/content.html', context)

def computingformathematics(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]

    all_course_list = Course.objects.all().order_by('-title')
    current_course_list = [c for c in all_course_list if c.currently_taught()]
    upcoming_course_list = [c for c in all_course_list if c.taught_soon()]

    context = {'all_course_list': all_course_list,
               'current_course_list': current_course_list,
               'news': news,
               'upcoming_course_list': upcoming_course_list,}


    return render_to_response('teaching/computingformathematics.html', context)

def pcutl(request):
    news = Item.objects.filter(published=True).order_by('-pub_date')[:5]
    return render_to_response('teaching/pcutl.html', {'news':news})
