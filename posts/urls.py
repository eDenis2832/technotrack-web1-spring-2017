from django.conf.urls import url, include
from .views import BlogsList, BlogView, PostView, CreateBlog, UpdateBlog, CreatePost, UpdatePost, CreateComment

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="editblog"),

    url(r'^posts/(?P<pk>\d+)/$', CreateComment.as_view(), name="createcomment"),
    url(r'^posts/(?P<pk>\d+)/edit$', login_required(UpdatePost.as_view()), name="editpost"),

    url(r'^$', BlogsList.as_view(), name="allblogs"),

    url(r'^addnewblog$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^addnewpost$', login_required(CreatePost.as_view()), name="createpost"),

]