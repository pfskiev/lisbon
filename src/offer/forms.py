from django import forms
from .models import Offer


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = [

            'title_PT',
            'title_EN',
            'title_DE',
            'position',
            'description_PT',
            'description_EN',
            'description_DE',
            'img',
            'keywords_SEO',
            'description_SEO',

        ]
