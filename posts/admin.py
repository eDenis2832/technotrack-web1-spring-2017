from django.contrib import admin
from .models import Blog
from .models import Post
from .models import Category

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Category)