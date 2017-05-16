import datetime
from django.db import models
from tours.models import Category, Tour
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class Article(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=1000, blank=True, null=False)
    category = models.ForeignKey(Category, default=None, blank=True, null=True)
    tour = models.ForeignKey(Tour, default=None, blank=True, null=True)
    link = models.URLField(max_length=100, blank=True, null=False)
    img = ThumbnailerImageField(_('Article thumbnail'), null=True, blank=True)
    keywords_SEO = models.TextField(_('Article keywords for SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Article description for SEO'), max_length=1000, blank=True, null=False)
    created_on = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def get_absolute_url(self):
        return reverse('news:detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('news:edit', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('news:delete', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

    class Meta:
        ordering = ['-created_on']

