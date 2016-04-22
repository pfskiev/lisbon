from django.db import models
from easy_thumbnails.fields import *
from autoslug.fields import *


class HotelCategory(models.Model):
    category = models.CharField(max_length=100, blank=True, null=False)
    url = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Hotel(models.Model):
    title_PT = models.CharField(max_length=100, blank=True, null=False)
    title_EN = models.CharField(max_length=100, blank=True, null=False)
    title_DE = models.CharField(max_length=100, blank=True, null=False)
    description_PT = models.TextField(max_length=1000, blank=True, null=False)
    description_EN = models.TextField(max_length=1000, blank=True, null=False)
    description_DE = models.TextField(max_length=1000, blank=True, null=False)
    category = models.ForeignKey(HotelCategory, default=1, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=False)
    trip_advisor = models.TextField(max_length=2000, blank=True, null=False)
    # tour = models.ForeignKey(Tour, default=1, blank=True, null=True)
    # link = models.URLField(max_length=100, blank=True, null=False)
    img = ThumbnailerImageField(null=True, blank=True)
    keywords_SEO = models.TextField(max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return "/rent-hotel/%i/" % self.id

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

