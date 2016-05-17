from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from autoslug.fields import AutoSlugField


class ContactHelpers(models.Model):
    pagination = models.IntegerField(_('Choose number of cards per Contacts page'), default=5)

    class Meta:
        verbose_name_plural = _('Contact helpers')

    def __str__(self):
        return _('Contact helpers')

    def __unicode__(self):
        return _('Contact helpers')


class Contact(models.Model):
    first_name = models.CharField(_('First name'), max_length=100, blank=True, null=False)
    first_name_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                             default=False)
    last_name = models.CharField(_('Last name'), max_length=100, blank=True, null=False)
    last_name_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                            default=False)
    short_bio = models.TextField(_('Short bio'), max_length=400, blank=True, null=False)
    short_bio_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                            default=False)
    img = models.FileField(_('Person photo'), null=True, blank=True)
    category = models.CharField(_('Staff category'), max_length=100, blank=True, null=False)
    category_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                           default=False)
    mobile = models.CharField(_('Mobile number'), max_length=100, blank=True, null=False)
    mobile_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    email = models.CharField(_('E-mail'), max_length=100, blank=True, null=False)
    email_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    whatsapp = models.CharField(_('Whatsapp number'), max_length=100, blank=True, null=False)
    whatsapp_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                           default=False)
    viber = models.CharField(_('Viber number'), max_length=100, blank=True, null=False)
    viber_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    telegram = models.CharField(_('Telegram number'), max_length=100, blank=True, null=False)
    telegram_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                           default=False)
    skype = models.CharField(_('Skype'), max_length=100, blank=True, null=False)
    skype_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    facebook = models.URLField(_('Facebook link'), max_length=100, blank=True, null=False)
    facebook_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                           default=False)
    twitter = models.URLField(_('Twitter link'), max_length=100, blank=True, null=False)
    twitter_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    pinterest = models.URLField(_('Pinterest link'), max_length=100, blank=True, null=False)
    pinterest_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                            default=False)
    google = models.URLField(_('Google + link'), max_length=100, blank=True, null=False)
    google_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'), default=False)
    instagram = models.URLField(_('Instagram link'), max_length=100, blank=True, null=False)
    instagram_preview = models.BooleanField(_('Apply if you wan\'t to show this field in contact card'),
                                            default=False)
    keywords_SEO = models.TextField(_('Keywords SEO'), max_length=1000, blank=True, null=False)
    description_SEO = models.TextField(_('Description SEO'), max_length=1000, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('contact:detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
