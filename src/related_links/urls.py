from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.related_links_list, name='list'),
    url(r'^create/$', views.related_links_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.related_links_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.related_links_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.related_links_delete, name='delete'),

]
