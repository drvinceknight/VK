import datetime
from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    def __unicode__(self):
        return self.title
    def currently_taught(self):
        now = timezone.now()
        return self.start_date <= now <  self.end_date
    def taught_soon(self):
        now = timezone.now()
        return self.start_date > now >= self.start_date - datetime.timedelta(days=21)
