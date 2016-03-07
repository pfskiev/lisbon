from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    img_main = models.FileField(null=True, blank=True)
    img_1 = models.FileField(null=True, blank=True)
    img_2 = models.FileField(null=True, blank=True)
    img_3 = models.FileField(null=True, blank=True)
    img_4 = models.FileField(null=True, blank=True)
    img_5 = models.FileField(null=True, blank=True)
    text = models.TextField(max_length=1000, blank=True, null=False)
    video = models.URLField(max_length=100, blank=True, null=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
