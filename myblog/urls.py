from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/$', views.blog_detail, name='blog_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]
