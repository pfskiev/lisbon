import re

from django import forms
from django.core.exceptions import ValidationError


def contains_html_tags(value):
    if re.search('<[^/>][^>]*>', value):
        raise ValidationError('Contains html tags.')


def contains_url(value):
    if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', value):
        raise ValidationError('Contains URL')
