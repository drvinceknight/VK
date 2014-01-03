import datetime
from django.db import models
from django.utils import timezone

class Paper(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateField('publication date')
    authors = models.TextField()
    abstract = models.TextField()
    journal = models.CharField(max_length=500, blank=True)
    volume = models.CharField(max_length=500, blank=True)
    issue = models.CharField(max_length=500, blank=True)
    pages = models.CharField(max_length=500, blank=True)
    keywords = models.TextField(blank=True)
    paperurl = models.URLField(max_length=200, blank=True)
    supplementaryurl = models.URLField(max_length=200, blank=True)
    supplementaryfile = models.FileField(upload_to="./research/supplementaryfiles", blank=True)
    openaccess = models.BooleanField()
    def published(self):
        if not self.pub_date:
            return False
        now = timezone.now()
        return self.pub_date <= now
    def __unicode__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    collaborators = models.TextField(blank=True)
    supplementaryurl = models.URLField(max_length=200, blank=True)
    supplementaryfile = models.FileField(upload_to="./research/supplementaryfiles", blank=True)
