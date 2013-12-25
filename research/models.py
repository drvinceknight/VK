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
    openaccess = models.BooleanField()
    def published(self):
        if not self.pub_date:
            return False
        now = timezone.now()
        return self.pub_date <= now
    def __unicode__(self):
        return self.title
