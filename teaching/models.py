import datetime
from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    endnote = models.TextField(blank=True)
    keywords = models.CharField(max_length=300, blank=True)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    slug = models.SlugField(unique=True, blank=True)
    def __unicode__(self):
        return self.title
    def currently_taught(self):
        now = timezone.now()
        return self.start_date <= now <  self.end_date
    def taught_soon(self):
        now = timezone.now()
        return self.start_date > now >= self.start_date - datetime.timedelta(days=21)

class Content(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    keywords = models.CharField(max_length=300, blank=True)

class HomeWork(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=200)
    description = models.TextField()
    hw = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    solutionpublished = models.BooleanField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    keywords = models.CharField(max_length=300, blank=True)

class ReadingListItem(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    relevance = models.FloatField(blank=True)
    class Meta:
        ordering = ['-relevance']
