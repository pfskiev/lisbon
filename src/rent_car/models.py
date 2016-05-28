from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from easy_thumbnails.fields import *
from autoslug.fields import *


class CarCategory(models.Model):
    category = models.CharField(max_length=100, blank=True, null=False)
    slug = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('rent_car:category', args=[str(self.slug)])

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Car(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=1000, blank=True, null=False)
    category = models.ForeignKey(CarCategory, default=1, blank=True, null=True)
    price = models.CharField(_('Price'), max_length=100, blank=True, null=False)
    # link = models.URLField(max_length=100, blank=True, null=False)
    img = ThumbnailerImageField(null=True, blank=True)
    keywords_SEO = models.TextField(_('Keywords for SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Description for SEO'), max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('rent_car:detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('rent_car:edit', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('rent_car:delete', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN
