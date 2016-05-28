from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class Helpers(models.Model):
    start_page_header_gb = models.CharField(max_length=200, blank=True, null=True)
    start_page_header_pt = models.CharField(max_length=200, blank=True, null=True)
    start_page_header_de = models.CharField(max_length=200, blank=True, null=True)
    copyright_gb = models.CharField(max_length=200, blank=True, null=True)
    copyright_pt = models.CharField(max_length=200, blank=True, null=True)
    copyright_de = models.CharField(max_length=200, blank=True, null=True)
    about_footer_PT = models.TextField(max_length=500, blank=True, null=False)
    about_footer_EN = models.TextField(max_length=500, blank=True, null=False)
    about_footer_DE = models.TextField(max_length=500, blank=True, null=False)
    footer_icon = models.FileField(blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    main_keywords = models.TextField(max_length=2000, blank=True, null=True)
    tour_header_name_PT = models.CharField(max_length=200, blank=True, null=True)
    tour_header_name_EN = models.CharField(max_length=200, blank=True, null=True)
    tour_header_name_DE = models.CharField(max_length=200, blank=True, null=True)
    offer_header_name_PT = models.CharField(max_length=200, blank=True, null=True)
    offer_header_name_EN = models.CharField(max_length=200, blank=True, null=True)
    offer_header_name_DE = models.CharField(max_length=200, blank=True, null=True)
    img = models.FileField(blank=True, null=True)
    img2 = models.FileField(blank=True, null=True)
    img3 = models.FileField(blank=True, null=True)
    img4 = models.FileField(blank=True, null=True)
    img5 = models.FileField(blank=True, null=True)
    audio = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return self.start_page_header_gb

    def __str__(self):
        return self.start_page_header_gb


class BaseClass(models.Model):
    title_PT = models.CharField(_('Title PT'), max_length=100, blank=True, null=False)
    title_EN = models.CharField(_('Title EN'), max_length=100, blank=True, null=False)
    title_DE = models.CharField(_('Title DE'), max_length=100, blank=True, null=False)
    description_PT = models.TextField(_('Description PT'), max_length=1000, blank=True, null=False)
    description_EN = models.TextField(_('Description EN'), max_length=1000, blank=True, null=False)
    description_DE = models.TextField(_('Description DE'), max_length=1000, blank=True, null=False)

    def __unicode__(self):
        return self.title_EN

    def __str__(self):
        return self.title_EN
