from django import forms
from django.forms import DateTimeField

from .models import Article


class ArticleForm(forms.ModelForm):
    created_on = DateTimeField(widget=forms.widgets.DateTimeInput())

    class Meta:
        model = Article
        fields = '__all__'
