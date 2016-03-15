from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.review_list, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.review_detail, name='detail'),
    url(r'^create/$', views.review_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.review_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.review_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.review_filter, name='filter'),
]
