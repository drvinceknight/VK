import datetime
from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date published')
    url = models.URLField(max_length=200)
    def __unicode__(self):
        return self.title
    def currently_taught(self):
        now = timezone.now()
        return self.start_date <= now <  self.end_date
    def taught_soon(self):
        now = timezone.now()
        return now - datetiel.tiemdelta(days=21) <= self.start_date <  now

