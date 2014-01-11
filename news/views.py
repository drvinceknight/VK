from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from news.models import Item

def index(request):
    allnews = Item.objects.filter(published=True).order_by('-pub_date')
    news = allnews[:5]

    context = {'allnews': allnews,
                'news': news,}

    return render_to_response('news/index.html', context)

def item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render_to_response('news/item.html', {'item': item})
