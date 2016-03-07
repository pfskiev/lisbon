from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.tour_list, name='tour_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.tour_detail, name='tour_detail'),
    url(r'^create/', views.tour_create, name='tour_create'),
    url(r'service/(?P<pk>[0-9]+)/$', views.ServiceDetailView.as_view(), name='service_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.tour_update, name='edit'),

)
