from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from autoslug.fields import AutoSlugField
from tours.models import Category, Tour
from rent_car.models import Car
from rent_hotel.models import Hotel


class OfferCategory(models.Model):
    category = models.CharField(_('Tours categories'), max_length=100, blank=True, null=False)
    slug = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('offer:category', args=[str(self.slug)])

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Offer(models.Model):
    category = models.ForeignKey(OfferCategory, default=None, blank=True, null=True)
    tour_category = models.ForeignKey(Category, default=None, blank=True, null=True)
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('description PT'), max_length=5000, blank=True, null=False)
    description_EN = models.TextField(_('description EN'), max_length=5000, blank=True, null=False)
    description_DE = models.TextField(_('description DE'), max_length=5000, blank=True, null=False)
    keywords_SEO = models.TextField(_('keywords for SEO'), max_length=5000, blank=True, null=False)
    description_SEO = models.TextField(_('description for SEO'), max_length=5000, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)
    img = models.ImageField(_('Offer thumbnail'), null=True, blank=True)
    position = models.IntegerField(_('Choose position of this offer to filter it on home page (number)'), default=1,
                                   blank=True, null=True)

    def get_absolute_url(self):
        return reverse('offer:detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('offer:edit', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('offer:delete', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

    class Meta:
        ordering = ['position', '-created_on']
