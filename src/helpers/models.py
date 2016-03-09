from django.db import models


class PTNavigation(models.Model):
    home = models.CharField(max_length=200, blank=True, null=True)
    tours = models.CharField(max_length=200, blank=True, null=True)
    review = models.CharField(max_length=200, blank=True, null=True)
    gallery = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.home

    def __str__(self):
        return self.home


class GBNavigation(models.Model):
    home = models.CharField(max_length=200, blank=True, null=True)
    tours = models.CharField(max_length=200, blank=True, null=True)
    review = models.CharField(max_length=200, blank=True, null=True)
    gallery = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.home

    def __str__(self):
        return self.home


class DENavigation(models.Model):
    home = models.CharField(max_length=200, blank=True, null=True)
    tours = models.CharField(max_length=200, blank=True, null=True)
    review = models.CharField(max_length=200, blank=True, null=True)
    gallery = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.home

    def __str__(self):
        return self.home


class Helpers(models.Model):
    start_page_header_gb = models.CharField(max_length=200, blank=True, null=True)
    start_page_header_pt = models.CharField(max_length=200, blank=True, null=True)
    start_page_header_de = models.CharField(max_length=200, blank=True, null=True)
    copyright_gb = models.CharField(max_length=200, blank=True, null=True)
    copyright_pt = models.CharField(max_length=200, blank=True, null=True)
    copyright_de = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.start_page_header_gb

    def __str__(self):
        return self.start_page_header_gb
