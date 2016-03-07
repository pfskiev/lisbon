from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.offer_list, name='list'),
    url(r'^create/$', views.offer_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.offer_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.offer_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.offer_delete, name='delete'),

]
