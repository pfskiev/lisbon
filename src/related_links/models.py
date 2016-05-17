from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class RelatedLink(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=1000, blank=True, null=False)
    link = models.URLField(_('Insert url to related link source'), max_length=100, blank=True, null=False)
    img = models.ImageField(_('Choose image'), null=True, blank=False)
    keywords_SEO = models.TextField(_('Keywords for SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Description for SEO'), max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('related_links:detail', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN

