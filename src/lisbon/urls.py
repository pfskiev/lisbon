from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [


    url(r'^', include('accounts.urls', namespace='accounts')),

    url(r'^users/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls, name='admin'),



    url(r'^$', views.start, name='start'),
    url(r'^de/$', views.home, name='home'),
    url(r'^pt/$', views.home, name='home'),
    url(r'^gb/$', views.home, name='home'),

    url(r'^gb/mail/', views.thankyou),

    url(r'^pt/tours/', include('tours.urls', namespace='tour_pt')),
    url(r'^gb/tours/', include('tours.urls', namespace='tour_gb')),
    url(r'^de/tours/', include('tours.urls', namespace='tour_de')),

    url(r'^reviews/', include('review.urls', namespace='review')),
    url(r'^pt/reviews/', include('review.urls', namespace='review')),
    url(r'^gb/reviews/', include('review.urls', namespace='review')),
    url(r'^de/reviews/', include('review.urls', namespace='review')),

    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^pt/gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^gb/gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^de/gallery/', include('gallery.urls', namespace='gallery')),

    url(r'^contacts/', include('contacts.urls', namespace='contact')),
    url(r'^pt/contacts/', include('contacts.urls', namespace='contact')),
    url(r'^gb/contacts/', include('contacts.urls', namespace='contact')),
    url(r'^de/contacts/', include('contacts.urls', namespace='contact')),


    url(r'^about/$', views.about, name='about'),
    url(r'^pt/about/$', views.about, name='about'),
    url(r'^gb/about/$', views.about, name='about'),
    url(r'^de/about/$', views.about, name='about'),

    url(r'^login-or-register/$', views.login_or_register, name='login_or_register'),
    url(r'^offer/', include('offer.urls', namespace='offer')),


]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
