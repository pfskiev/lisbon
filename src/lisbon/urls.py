from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gb/$', views.home, name='home'),
    url(r'^de/$', views.home, name='home'),


    # url(r'^/$', views.home, name='home'),
    # url(r'^$', views.home, name='home'),
    # url(r'^$', views.home, name='home'),


    url(r'^create/', views.post_create, name='create_review'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contact_list, name='contacts'),
    url(r'^gallery/$', views.gallery_list, name='gallery'),
    url(r'^reviews/$', views.review_list, name='review_list'),
    url(r'^users/', include('profiles.urls', namespace='profiles')),




    url(r'^tours/', include('tours.urls')),




    url(r'^', include('accounts.urls', namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
