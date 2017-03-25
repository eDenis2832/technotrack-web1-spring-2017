from django.conf.urls import url, include
from django.contrib.auth.views import login, logout


from .views import HomePageView, register

urlpatterns = [
    #url(r'^(?P<post_id>\d+)/$', test),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),
    url(r'^$', HomePageView.as_view(), name='home'),
]
