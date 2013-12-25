from django.http import HttpResponse

def detail(request, paper_id):
    return HttpResponse("Hello world")
