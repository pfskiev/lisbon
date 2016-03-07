from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=False)
    img = models.FileField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, null=False)
    mobile = models.CharField(max_length=100, blank=True, null=False)
    email = models.CharField(max_length=100, blank=True, null=False)
    whatsapp = models.CharField(max_length=100, blank=True, null=False)
    viber = models.CharField(max_length=100, blank=True, null=False)
    telegram = models.CharField(max_length=100, blank=True, null=False)
    skype = models.CharField(max_length=100, blank=True, null=False)
    facebook = models.URLField(max_length=100, blank=True, null=False)
    twitter = models.URLField(max_length=100, blank=True, null=False)
    pinterest = models.URLField(max_length=100, blank=True, null=False)
    google = models.URLField(max_length=100, blank=True, null=False)
    instagram = models.URLField(max_length=100, blank=True, null=False)

    def __str__(self):
        return self.last_name

    def __unicode__(self):
        return self.last_name
