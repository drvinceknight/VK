from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    published = models.BooleanField(default=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __unicode__(self):
        return u'%s' % self.title
