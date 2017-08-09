from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from autoslug.fields import AutoSlugField


class BaseClass(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=5000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=5000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=5000, blank=True, null=False)
    keywords_SEO = models.TextField(_('Keywords for SEO'), max_length=2000, blank=True, null=False)
    description_SEO = models.TextField(_('Description for SEO'), max_length=2000, blank=True, null=False)

    class Meta:
        abstract = True
        ordering = ['name']


class Category(models.Model):
    category = models.CharField(_('Tours categories'), max_length=100, blank=True, null=False)
    url = AutoSlugField(populate_from='category', unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('tour:category', args=[str(self.url)])

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Tour(BaseClass):
    category = models.ForeignKey(Category, default=1, blank=True, null=True)
    short_description_EN = models.TextField(_('Short description EN'), max_length=5000, blank=True, null=False)
    short_description_DE = models.TextField(_('Short description DE'), max_length=5000, blank=True, null=False)
    short_description_PT = models.TextField(_('Short description PT'), max_length=5000, blank=True, null=False)
    price = models.CharField(_('Tour price'), max_length=100, blank=True, null=False)
    img = models.FileField(_('Tour thumbnail'), null=True, blank=True)
    url = models.URLField(_('Tour thumbnail URL'), max_length=200, blank=True, null=False)
    created_on = models.DateTimeField(_('Creation date'), auto_now_add=True, auto_created=False)
    position = models.IntegerField(_('Position'), default=1, blank=True, null=True)

    class Meta:
        ordering = ['position', '-created_on']
        verbose_name_plural = _('Tour')

    def get_absolute_url(self):
        return reverse('tour:detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('tour:edit', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('tour:delete', args=[str(self.id)])

    def __str__(self):
        return self.title_EN

    def __unicode__(self):
        return self.title_EN


class Paragraph(models.Model):
    text_PT = models.TextField(max_length=500, blank=True, null=False)
    text_EN = models.TextField(max_length=500, blank=True, null=False)
    text_DE = models.TextField(max_length=500, blank=True, null=False)

    def __str__(self):
        return self.text_EN

    def __unicode__(self):
        return self.text_EN


class About(models.Model):
    paragraph = models.ManyToManyField(Paragraph)
    keywords_SEO = models.TextField(max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(max_length=1000, blank=True, null=False)

    def __str__(self):
        return _('Paragraph')

    def __unicode__(self):
        return _('Paragraph')
