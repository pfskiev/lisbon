from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=False)
    first_name_preview = models.BooleanField(default=False)
    last_name = models.CharField(max_length=100, blank=True, null=False)
    last_name_preview = models.BooleanField(default=False)
    short_bio = models.TextField(max_length=400, blank=True, null=False)
    short_bio_preview = models.BooleanField(default=False)
    img = models.FileField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, null=False)
    category_preview = models.BooleanField(default=False)
    mobile = models.CharField(max_length=100, blank=True, null=False)
    mobile_preview = models.BooleanField(default=False)
    email = models.CharField(max_length=100, blank=True, null=False)
    email_preview = models.BooleanField(default=False)
    whatsapp = models.CharField(max_length=100, blank=True, null=False)
    whatsapp_preview = models.BooleanField(default=False)
    viber = models.CharField(max_length=100, blank=True, null=False)
    viber_preview = models.BooleanField(default=False)
    telegram = models.CharField(max_length=100, blank=True, null=False)
    telegram_preview = models.BooleanField(default=False)
    skype = models.CharField(max_length=100, blank=True, null=False)
    skype_preview = models.BooleanField(default=False)
    facebook = models.URLField(max_length=100, blank=True, null=False)
    facebook_preview = models.BooleanField(default=False)
    twitter = models.URLField(max_length=100, blank=True, null=False)
    twitter_preview = models.BooleanField(default=False)
    pinterest = models.URLField(max_length=100, blank=True, null=False)
    pinterest_preview = models.BooleanField(default=False)
    google = models.URLField(max_length=100, blank=True, null=False)
    google_preview = models.BooleanField(default=False)
    instagram = models.URLField(max_length=100, blank=True, null=False)
    instagram_preview = models.BooleanField(default=False)
    keywords_SEO = models.TextField(max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return "/contacts/%i/" % self.id

    def __str__(self):
        return self.last_name

    def __unicode__(self):
        return self.last_name
