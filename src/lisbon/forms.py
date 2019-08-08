import re

from django import forms
from django.core.exceptions import ValidationError


def contains_html_tags(value):
    if re.search('<[^/>][^>]*>', value):
        raise ValidationError('Contains html tags.')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, validators=[contains_html_tags])
    email = forms.EmailField(max_length=100, required=True, validators=[contains_html_tags])
    message = forms.CharField(max_length=100, required=True, validators=[contains_html_tags])
    additional_information = forms.CharField(max_length=0, required=False, validators=[contains_html_tags])
