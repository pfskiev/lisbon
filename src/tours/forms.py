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
            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'price',
            'img',
            'url',
            'keywords_SEO',
            'description_SEO',

        ]


class BookNow(forms.Form):

    fullname = forms.CharField(label=_('Name'), required=True)
    tour = forms.ModelChoiceField(label=_('Tour'), required=True, queryset=Tour.objects.all())
    # card_number = forms.CharField(label="Card", required=True, max_length=16)
    phone = forms.IntegerField(label=_('Phone'), required=True)
    from_date = forms.DateField(label=_('From Date'), required=True)
    to_date = forms.DateField(label=_('From Date'), required=True)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(), required=True)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('fullname', css_class='form-control'),
        Field('tour', css_class='form-control'),
        Field('phone', css_class='form-control'),
        Field('message', css_class='form-control'),
        Field('from_date', css_class='datepicker'),
        Field('to_date', css_class='datepicker'),
        FormActions(Submit('purchase', _('confirm'), css_class='text-uppercase form-control btn btn-lg btn-primary'))
    )
