from django.conf.urls import url
from . import views
from .models import Category

urlpatterns = (

    url(r'^$', views.tour_list, name='list'),
    url(r'^create/', views.tour_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.tour_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.tour_update, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.tour_delete, name='delete'),

)

# categories = Category.objects.all()
# for category in categories:
#     urlpatterns += url(r'^' + category.url, views.tour_category, name=category.url),

