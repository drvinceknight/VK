from django.db import models

class UsefullLink(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    category = models.CharField(max_length=500,blank=True)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return self.title

class LettersOfRecommendation(models.Model):
    name = models.CharField(max_length=500)
    target = models.CharField(max_length=500, blank=True)
    author = models.CharField(max_length=500, default='Vincent Knight')
    signature = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False, blank=True)
    pub_date = models.DateTimeField()
    url = models.URLField(max_length=500, blank=True)
    pdf = models.URLField(max_length=500, blank=True)
    def __unicode__(self):
        return "By %s for %s" % (self.author, self.name)

class PC(models.Model):
    name = models.CharField(max_length=500, blank=True)
    def __unicode__(self):
        return self.name

class Component(models.Model):
    PC = models.ForeignKey(PC)
    title = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)

class MediaAppearance(models.Model):
    name = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(blank=True)
    url = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return "%s - %s" % (self.date, self.name)
    class Meta:
        ordering = ['-date']
