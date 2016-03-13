from django.contrib.sitemaps import Sitemap

from tours.models import Tour
from contacts.models import Contact
from gallery.models import Gallery
from review.models import Review
from offer.models import Offer


class TodoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Tour.objects.all()


class ContactSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Contact.objects.all()


class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Gallery.objects.all()


class OfferSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Offer.objects.all()


class ReviewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Review.objects.all()


sitemaps = {
    'tour': TodoSitemap(),
    'contact': ContactSitemap(),
    'gallery': GallerySitemap(),
    'offer': OfferSitemap(),
    'review': ReviewSitemap(),
}