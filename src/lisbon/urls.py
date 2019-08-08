from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from . import views
from .sitemap import sitemaps

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^BingSiteAuth\.xml$', TemplateView.as_view(template_name="BingSiteAuth.xml", content_type="text/xml"), name="BingSiteAuth"),
    url(r'^googled15ef6cfc26e20bd\.html$', TemplateView.as_view(template_name="googled15ef6cfc26e20bd.html", content_type="text/html"), name="googled15ef6cfc26e20bd"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^users/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^tours/', include('tours.urls', namespace='tour')),
    url(r'^reviews/', include('review.urls', namespace='review')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^contacts/', include('contacts.urls', namespace='contact')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^rent-car/', include('rent_car.urls', namespace='rent_car')),
    url(r'^rent-hotel/', include('rent_hotel.urls', namespace='rent_hotel')),
    url(r'^about/$', views.about, name='about'),
    url(r'^book-form/$', views.book_form, name='book_form'),
    url(r'^login-or-register/$', views.login_or_register, name='login_or_register'),
    url(r'^offers/', include('offer.urls', namespace='offer')),
    url(r'^category/', include('category.urls', namespace='category')),
    url(r'^related-links/', include('related_links.urls', namespace='related_links')),
    url(r'^booking/', include('booking.urls', namespace='booking')),
    url(r'^search/$', views.search, name='search'),
    url(r'^welcome/$', views.welcome, name='welcome'),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
