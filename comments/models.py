from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from posts.models import Post

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    post = models.ForeignKey(Post)
