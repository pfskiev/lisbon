from django.conf.urls import url
from . import views

urlpatterns = (

    url(r'^$', views.rent_car_list, name='list'),
    # url(r'^create/$', views.rent_car_create, name='create'),
    # url(r'^(?P<pk>[0-9]+)/$', views.rent_car_detail, name='detail'),
    # url(r'^(?P<pk>[0-9]+)/edit/$', views.rent_car_update, name='edit'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.rent_car_delete, name='delete'),
    # # url(r'^(?P<slug>[\w-]+)/$', views.rent_car_category, name='cat'),

)


