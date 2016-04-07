from django.conf.urls import url
from . import views

urlpatterns = (

    url(r'^$', views.news_list, name='list'),
    url(r'^create/$', views.news_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.news_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.news_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.news_delete, name='delete'),
    # url(r'^(?P<slug>[\w-]+)/$', views.news_category, name='cat'),

)


