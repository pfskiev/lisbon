from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [

            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'category',
            'price',
            'img',
            'keywords_SEO',
            'description_SEO',

        ]
