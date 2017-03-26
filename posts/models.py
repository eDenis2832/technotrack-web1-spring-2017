from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.TextField()

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    categories = models.ManyToManyField(Category)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    likes = models.IntegerField()






