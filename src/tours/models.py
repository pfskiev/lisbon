from django.db import models


class Tour(models.Model):
    title_pt = models.CharField(max_length=100, blank=True, null=False)
    title_gb = models.CharField(max_length=100, blank=True, null=False)
    title_de = models.CharField(max_length=100, blank=True, null=False)
    description_pt = models.TextField(max_length=1000, blank=True, null=False)
    description_gb = models.TextField(max_length=1000, blank=True, null=False)
    description_de = models.TextField(max_length=1000, blank=True, null=False)
    price = models.CharField(max_length=100, blank=True, null=False)
    img = models.FileField(null=True, blank=True)
    url = models.URLField(max_length=200, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)

    def get_absolute_url(self):
        return "/tour/%i/" % self.id

    def __str__(self):
        return self.title_pt

    def __unicode__(self):
        return self.title_pt


class Paragraph(models.Model):
    text = models.TextField(max_length=500, blank=True, null=False)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class About(models.Model):
    paragraph = models.ManyToManyField(Paragraph)

    # def __str__(self):
    #     return self.paragraph

    def __unicode__(self):
        return self.paragraph
