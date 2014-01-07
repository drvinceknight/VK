from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from blog.models import Post

def index(request):
    posts = Post.objects.filter(published=True)
    return render_to_response('blog/index.html', {'posts':posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/post.html', {'post': post})
