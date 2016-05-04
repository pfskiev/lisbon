from django.db import models
from easy_thumbnails.fields import *
from autoslug.fields import *
from django.utils.translation import ugettext as _


class HotelCategory(models.Model):
    category = models.CharField(max_length=100, blank=True, null=False)
    url = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Hotel(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Hotel description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Hotel description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Hotel description DE'), max_length=1000, blank=True, null=False)
    category = models.ForeignKey(HotelCategory, default=1, blank=True, null=True)
    price = models.CharField(_('Hotel price per day'), max_length=100, blank=True, null=False)
    trip_advisor_PT = models.TextField(_('Input script for widget from TripAdvisor PT'), max_length=2000, blank=True,
                                       null=False)
    trip_advisor_EN = models.TextField(_('Input script for widget from TripAdvisor EN'), max_length=2000, blank=True,
                                       null=False)
    trip_advisor_DE = models.TextField(_('Input script for widget from TripAdvisor DE'), max_length=2000, blank=True,
                                       null=False)
    # tour = models.ForeignKey(Tour, default=1, blank=True, null=True)
    # link = models.URLField(max_length=100, blank=True, null=False)
    img = ThumbnailerImageField(_('Hotel thumbnail'), null=True, blank=True)
    keywords_SEO = models.TextField(_('Hotel keywords for SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Hotel description for SEO'), max_length=1000, blank=True, null=False)

    class Meta:
        # ordering = ['position', '-created_on']
        verbose_name_plural = _('Hotel')

    def get_absolute_url(self):
        return '/rent-hotel/%i/' % self.id

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN
