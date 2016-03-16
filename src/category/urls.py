from django.conf.urls import url
from . import views

urlpatterns = (

    # url(r'^$', views.category_list, name='list'),
    # url(r'^create/', views.category_create, name='create'),
    # url(r'^(?P<pk>[0-9]+)/$', views.category_detail, name='detail'),
    # url(r'^(?P<pk>[0-9]+)/edit/$', views.category_update, name='edit'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.category_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.category_list, name='list'),

)

