from django.conf import settings
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text
