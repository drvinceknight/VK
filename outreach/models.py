from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    published = models.BooleanField(default=True, blank=True)
    date_added = models.DateTimeField(blank=True, null=True)
    url = models.URLField(max_length=500, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'%s' % self.title

class Activity(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(blank=True)
