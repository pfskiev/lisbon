from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.gallery_list, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.gallery_detail, name='detail'),
    url(r'^create/$', views.gallery_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.gallery_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.gallery_delete, name='delete'),

]