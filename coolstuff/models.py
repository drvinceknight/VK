from django.db import models

class UsefullLink(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    category = models.CharField(max_length=500,blank=True)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return self.title
