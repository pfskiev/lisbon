from django import forms

from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [

            'title',
            'img_main',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'img_5',
            'text',
            'video',

        ]
