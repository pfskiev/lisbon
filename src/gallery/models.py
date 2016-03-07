from django.db import models


class Gallery(models.Model):
    img = models.FileField(null=True, blank=True)
    title = models.TextField(max_length=1000, blank=True, null=False)
    video = models.URLField(max_length=100, blank=True, null=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
