from django.conf.urls import include, url
from myblog import views

urlpatterns = [
    url(r'^(?P<pindex>\d*)$', views.index),
    url(r'^post/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<id>[0-9]+)/(?P<pindex>\d*)$', views.category, name='category'),

    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<pindex>\d*)$', views.archives, name='archives'),
]
