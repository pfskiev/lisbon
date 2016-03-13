from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    text = models.TextField(max_length=1000, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)
    img = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return "/offers/%i/" % self.id

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
