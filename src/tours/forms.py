from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [

            'title_pt',
            'title_gb',
            'title_de',
            'description_pt',
            'description_gb',
            'description_de',
            'price',
            'img',
            'url',

        ]

