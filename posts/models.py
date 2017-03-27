from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.TextField()
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    categories = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    #likes = models.IntegerField()
    def __unicode__(self):
        return self.title + " / " + self.blog.title

class Like(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return "from " + self.author.__unicode__() + " to " + self.post.__unicode__()





