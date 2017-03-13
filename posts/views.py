from django.shortcuts import render
from .models import Blog, Post
from django.views.generic import ListView, DetailView
from comments.models import Comment

class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = "posts/blogs.html"


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "posts/blog.html"

class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post.html"



'''
def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'posts/blogs.html', {'blogs': blogs})
'''

'''
def show_blog(request, blog_id=None):
    blog = Blog.objects.get(id=blog_id)
    posts = Post.objects.filter(blog=blog)
    return render(request, 'posts/blog.html', {'blog': blog, 'posts': posts})
'''