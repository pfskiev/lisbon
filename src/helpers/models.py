from django.db import models


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
