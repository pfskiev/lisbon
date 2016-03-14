from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [

            # 'category',
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

