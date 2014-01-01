from django.db import models

class UsefullLink(models.Model)
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=200, blank=True)
    description = models.TextField()
