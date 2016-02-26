from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.tour_list, name='tour_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TourDetailView.as_view(), name='tour_detail'),
)
