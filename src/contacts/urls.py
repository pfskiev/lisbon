from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact_list, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.contact_detail, name='detail'),
    url(r'^create/$', views.contact_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.contact_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.contact_delete, name='delete'),

]
