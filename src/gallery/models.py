from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class Gallery(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=1000, blank=True, null=False)
    img = models.ImageField(_('Photo # 1'), null=True, blank=True)
    img_1 = models.ImageField(_('Photo # 2'), null=True, blank=True)
    img_2 = models.ImageField(_('Photo # 3'), null=True, blank=True)
    img_3 = models.ImageField(_('Photo # 4'), null=True, blank=True)
    img_4 = models.ImageField(_('Photo # 5'), null=True, blank=True)
    img_5 = models.ImageField(_('Photo # 5'), null=True, blank=True)
    video = models.URLField(_('Video url'), max_length=100, blank=True, null=False)
    keywords_SEO = models.TextField(_('Keywords SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Description SEO'), max_length=1000, blank=True, null=False)

    class Meta:
        verbose_name_plural = _('Gallery')

    def get_absolute_url(self):
        return reverse('gallery:detail', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN
