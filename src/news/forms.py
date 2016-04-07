from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [

            'title_PT',
            'title_EN',
            'title_DE',
            'description_PT',
            'description_EN',
            'description_DE',
            'link',
            'img',
            'keywords_SEO',
            'description_SEO',

        ]
