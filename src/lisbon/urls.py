from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^users/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^tours/', include('tours.urls')),
    url(r'^contacts/', include('contacts.urls', namespace='contact')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^reviews/', include('review.urls', namespace='review')),
    url(r'^about/$', views.about, name='about'),
    url(r'^login-or-register/$', views.login_or_register, name='login_or_register')

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
