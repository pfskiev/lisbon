from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^pricing/$', views.PricingPage.as_view(), name='pricing'),
    url(r'^users/', include('profiles.urls', namespace='profiles')),
    url(r'^tours/', include('tours.urls')),
    url(r'^', include('accounts.urls', namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
