from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from autoslug.fields import AutoSlugField
from tours.models import Category, Tour
from rent_car.models import Car
from rent_hotel.models import Hotel


class OfferCategory(models.Model):
    category = models.CharField(_('Tours categories'), max_length=100, blank=True, null=False)
    url = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def get_absolute_url(self):
        return "/offer/%s/" % self.url

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Offer(models.Model):
    title_PT = models.CharField(max_length=100, blank=True, null=False)
    title_EN = models.CharField(max_length=100, blank=True, null=False)
    title_DE = models.CharField(max_length=100, blank=True, null=False)
    description_PT = models.TextField(max_length=1000, blank=True, null=False)
    description_EN = models.TextField(max_length=1000, blank=True, null=False)
    description_DE = models.TextField(max_length=1000, blank=True, null=False)
    keywords_SEO = models.TextField(max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(max_length=1000, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)
    img = models.ImageField(null=True, blank=True)
    position = models.IntegerField(default=1, blank=True, null=True)
    category = models.ForeignKey(OfferCategory, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return "/offer/%i/" % self.id

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

    class Meta:
        ordering = ['position', '-created_on']