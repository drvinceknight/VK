from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=True, blank=True)
    pubdate = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
