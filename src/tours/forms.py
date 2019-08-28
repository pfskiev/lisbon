from django import forms
from django.utils.translation import ugettext_lazy as _

from lisbon.forms import contains_html_tags, contains_url
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [

            'category',
            'position',
            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'short_description_PT',
            'short_description_EN',
            'short_description_DE',
            'price',
            'img',
            'url',
            'keywords_SEO',
            'description_SEO',

        ]


class BookNow(forms.Form):
    fullname = forms.CharField(label=_('Name'), required=True, validators=[contains_html_tags, contains_url])
    email = forms.EmailField(label=_('Email'), required=True, validators=[contains_html_tags, contains_url])
    phone = forms.CharField(label=_('Phone'), required=True, validators=[contains_html_tags, contains_url])
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(), required=True,
                              validators=[contains_html_tags, contains_url])
    date = forms.DateField(label=_('From Date'), required=True)


class ContactMe(forms.Form):
    fullname = forms.CharField(label=_('Name'), required=True, validators=[contains_html_tags, contains_url])
    email = forms.EmailField(label=_('Email'), required=True, validators=[contains_html_tags, contains_url])
    phone = forms.CharField(label=_('Phone'), required=True, validators=[contains_html_tags, contains_url])
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(), required=True,
                              validators=[contains_html_tags, contains_url])
