from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from .models import Tour
from django.utils.translation import ugettext_lazy as _


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

    fullname = forms.CharField(label=_('Name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)
    phone = forms.CharField(label=_('Phone'), required=True)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(), required=True)
    date = forms.DateField(label=_('From Date'), required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('fullname', css_class='form-control', placeholder='Enter you\'re name'),
        Field('email', css_class='form-control', placeholder='Enter you\'re email'),
        Field('phone', css_class='phone', placeholder='(000)-00-000-00-00'),
        Field('message', css_class='form-control'),
        Field('date', css_class='datepicker'),
        FormActions(Submit('purchase', _('Send'), css_class='text-uppercase form-control btn btn-lg btn-primary'))
    )


class ContactMe(forms.Form):

    fullname = forms.CharField(label=_('Name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)
    phone = forms.CharField(label=_('Phone'), required=True)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(), required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('fullname', css_class='form-control', placeholder='Enter you\'re name'),
        Field('email', css_class='form-control', placeholder='Enter you\'re email'),
        Field('phone', css_class='form-control', placeholder='Enter you\'re phone'),
        Field('message', css_class='form-control'),
        FormActions(Submit('purchase', _('Send'), css_class='text-uppercase form-control btn btn-lg btn-primary'))
    )
