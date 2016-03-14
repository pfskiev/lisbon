from django import forms

from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [

            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'img',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'img_5',
            'video',
            'keywords_SEO',
            'description_SEO',

        ]
