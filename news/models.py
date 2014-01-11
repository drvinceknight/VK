from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    published = models.BooleanField(default=False, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    url = models.URLField(max_length=200, blank=True)
    def __unicode__(self):
        return self.title
