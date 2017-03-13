from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog)
    text = models.TextField()


