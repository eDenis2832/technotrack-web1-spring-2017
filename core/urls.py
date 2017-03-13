from django.conf.urls import url, include
from core.views import test

urlpatterns = [
    url(r'^(?P<post_id>\d+)/$', test),
]
