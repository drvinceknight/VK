import datetime
from django.db import models
from django.utils import timezone

class Paper(models.Model):
    title = models.CharField(max_length=500)
    journal = models.CharField(max_length=500, blank=True)
    volume = models.CharField(max_length=500, blank=True)
    issue = models.CharField(max_length=500, blank=True)
    pages = models.CharField(max_length=500, blank=True)
    pub_date = models.DateField('publication date', blank=True)
    authors = models.TextField()
    abstract = models.TextField()
    keywords = models.TextField()
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
