from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify


class Tour(models.Model):
    title_pt = models.CharField(max_length=100, blank=True, null=False)
    title_en = models.CharField(max_length=100, blank=True, null=False)
    title_de = models.CharField(max_length=100, blank=True, null=False)
    text = models.TextField(max_length=1000, blank=True, null=False)
    url = models.URLField(max_length=200, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title_pt

    def __unicode__(self):
        return self.title_pt


class Offer(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    text = models.TextField(max_length=1000, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=False)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Gallery(models.Model):
    img = models.FileField(null=True, blank=True)
    title = models.TextField(max_length=100, blank=True, null=False)
    video = models.URLField(max_length=1000, blank=True, null=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


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
        return self.name


# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.objects.all() = super(PostManager, self).all()
#         return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("review_list")
