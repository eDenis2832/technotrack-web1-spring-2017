from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from posts.models import Blog, Post
from comments.models import Comment


from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.views.generic.base import TemplateView

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_count'] = Blog.objects.all().count()
        context['posts_count'] = Post.objects.all().count()
        context['comments_count'] = Comment.objects.all().count()
        #context['comments_count']
        return context



def register(request):
    if request.method == 'GET':
        form = MyUserCreationForm()
    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect("/")
    return render(request, 'core/register.html', {'form': form})

'''
kmo
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/books/")
    else:
        data, errors = {}, {}

    return render_to_response("registration/register.html", {
        'form' : forms.FormWrapper(form, data, errors)
    })


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
'''