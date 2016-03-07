from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^users/', include('profiles.urls', namespace='profiles')),
    url(r'^', include('accounts.urls', namespace='accounts')),

    url(r'^tours/', include('tours.urls')),
    url(r'^contacts/', include('contacts.urls', namespace='contact')),

    
    url(r'^create/', views.feedback_create, name='create_review'),
    url(r'^feedback/(?P<pk>[0-9]+)/details/$', views.feedback_edit.as_view(), name='feedback_detail'),

    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about, name='about'),


    url(r'^gallery/$', views.gallery_list, name='gallery'),
    url(r'^reviews/$', views.review_list, name='review_list'),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
