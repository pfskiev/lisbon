from django.conf.urls import url
from . import views

urlpatterns = (

    url(r'^$', views.tour_list, name='list'),
    url(r'^create/$', views.tour_create, name='create'),
    url(r'^success/$', views.tour_success, name='success'),
    url(r'^fail/$', views.tour_fail, name='fail'),
    url(r'^(?P<pk>[0-9]+)/$', views.tour_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.tour_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.tour_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.tour_category, name='category'),

)


