from django import forms

from .models import RelatedLink


class RelatedLinkForm(forms.ModelForm):
    class Meta:
        model = RelatedLink
        fields = [

            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'link',
            'img',
            'html',
            'keywords_SEO',
            'description_SEO',

        ]

    def __init__(self, *args, **kwargs):
        super(RelatedLinkForm, self).__init__(*args, **kwargs)
        self.fields['img'].required = True
