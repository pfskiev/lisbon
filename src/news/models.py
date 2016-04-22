from django.db import models
from tours.models import Category, Tour
from easy_thumbnails.fields import ThumbnailerImageField


class Article(models.Model):
    title_PT = models.CharField(max_length=100, blank=True, null=False)
    title_EN = models.CharField(max_length=100, blank=True, null=False)
    title_DE = models.CharField(max_length=100, blank=True, null=False)
    description_PT = models.TextField(max_length=1000, blank=True, null=False)
    description_EN = models.TextField(max_length=1000, blank=True, null=False)
    description_DE = models.TextField(max_length=1000, blank=True, null=False)
    category = models.ForeignKey(Category, default=1, blank=True, null=True)
    tour = models.ForeignKey(Tour, default=1, blank=True, null=True)
    link = models.URLField(max_length=100, blank=True, null=False)
    img = ThumbnailerImageField(null=True, blank=True)
    keywords_SEO = models.TextField(max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return "/news/%i/" % self.id

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

