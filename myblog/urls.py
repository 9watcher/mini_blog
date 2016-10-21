from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<blog_id>[0-9]+)/$', views.blog_detail, name='blog_detail'),
]
