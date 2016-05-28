from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from tours.models import Tour


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Tour, default=1, blank=True, null=True)
    review = models.TextField(max_length=1000, blank=True, null=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('review:detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('review:edit', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('review:delete', args=[str(self.id)])

    def __unicode__(self):
        return self.review

    def __str__(self):
        return self.review
