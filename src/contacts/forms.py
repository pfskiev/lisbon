from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [

            'first_name',
            'first_name_preview',
            'last_name',
            'last_name_preview',
            'img',
            'category',
            'category_preview',
            'mobile',
            'mobile_preview',
            'email',
            'email_preview',
            'whatsapp',
            'whatsapp_preview',
            'viber',
            'viber_preview',
            'telegram',
            'telegram_preview',
            'skype',
            'skype_preview',
            'facebook',
            'facebook_preview',
            'twitter',
            'twitter_preview',
            'pinterest',
            'pinterest_preview',
            'google',
            'google_preview',
            'instagram',
            'instagram_preview'
        ]