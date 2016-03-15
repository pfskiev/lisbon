from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from tours.models import Tour
from contacts.models import Contact
from gallery.models import Gallery
from review.models import Review
from offer.models import Offer


class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'hourly'

    def items(self):
        return ['home', 'tour:list', 'contact:list', 'review:list', 'offer:list']

    def location(self, item):
        return reverse(item)


class TourSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Tour.objects.all()


class ContactSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Contact.objects.all()


class GallerySitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Gallery.objects.all()


class OfferSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Offer.objects.all()


class ReviewSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Review.objects.all()


sitemaps = {
    'static': StaticSitemap(),
    'tours': TourSitemap(),
    'contact': ContactSitemap(),
    'gallery': GallerySitemap(),
    'offer': OfferSitemap(),
    'review': ReviewSitemap(),
}
