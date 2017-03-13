from django.conf.urls import url, include
from .views import BlogsList, BlogView, PostView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),

    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="onepost"),

    url(r'^$', BlogsList.as_view(), name="allblogs"),

]