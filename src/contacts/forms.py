from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [

            'first_name',
            'last_name',
            'img',
            'category',
            'mobile',
            'email',
            'whatsapp',
            'viber',
            'telegram',
            'skype',
            'facebook',
            'twitter',
            'pinterest',
            'google',
            'instagram',

        ]