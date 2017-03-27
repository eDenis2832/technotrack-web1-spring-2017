from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from comments.models import Comment
from django.urls import reverse_lazy



from django import forms


class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(('title', 'Title'),
                                      ('description', 'Description'),
                                      ('rate', 'Rate'),
                                      ))
    search = forms.CharField(required=False)

'''
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'rate')
'''


class CreateBlog(CreateView):
    template_name = 'posts/addblog.html'
    model = Blog
    fields = ('title', 'description', 'categories')
    def get_success_url(self):
        return reverse_lazy('posts:allblogs')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)

class UpdateBlog(UpdateView):
    template_name = 'posts/editblog.html'
    model = Blog
    fields = ('title', 'description')
    pk = int
    def get_success_url(self):
        return reverse_lazy('posts:oneblog', kwargs={'pk':self.pk})
    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super(UpdateBlog, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)

class CreatePost(CreateView):
    template_name = 'posts/addpost.html'
    model = Post
    fields = ('title', 'blog', 'text')

    def get_success_url(self):
        return reverse_lazy('posts:allblogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)
'''
    def get_form(self, form_class):
        form = super(CreatePost, self).get_form(self, from_class=form_class)
        form.fields["blog"].queryset = form.fields["blog"].queryset.filter(author=self.request.user)
        return form
'''
    #def get_form(self, form_class=None):
    #    self.fields["blog"].queryset = self.fields["blog"].queryset.filter(author=self.request.user)
     #   return super(CreatePost, self).get_form()

class UpdatePost(UpdateView):
    template_name = 'posts/editpost.html'
    model = Post
    fields = ('title', 'text')
    pk = int
    def get_success_url(self):
        return reverse_lazy('posts:createcomment', kwargs={'pk':self.pk})

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super(UpdatePost, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)

class CreateComment(CreateView):
    template_name = "posts/post.html"
    model = Comment
    fields = ('text', )
    postob=None
    pk = int
    def get_success_url(self):
        return reverse_lazy('posts:createcomment', kwargs={'pk':self.pk})
    def dispatch(self, request, *args, **kwargs):
        self.postob = get_object_or_404(Post, id=kwargs['pk'])
        self.pk = kwargs['pk']
        return super(CreateComment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateComment, self).get_context_data(**kwargs)
        context['post'] = self.postob
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postob
        return super(CreateComment, self).form_valid(form)


class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = "posts/blogs.html"
    sortform=None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):  #info about objects
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "posts/blog.html"




'''
def createblog(request):
    if request.method == 'GET':
        form = BlogForm(initial={'title':"Enter title"})
    elif request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = Blog(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            blog.author = request.user;
            blog.rate = 0
            blog.save()
            return redirect('/blogs/')
    return render(request, 'posts/addblog.html', {'form': form})


def updateblog(request, pk=None):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'GET':
        form = BlogForm(instance=blog)
    elif request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/blogs/')
    return render(request, 'posts/editblog.html', {'form': form})
'''




'''
class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post.html"




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


