from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from helpers.models import Helpers
from offer.models import Offer
from tours.models import Category, Tour, About
from offer.models import OfferCategory
from tours.forms import BookNow, ContactMe


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def home(request):
    lang = request.LANGUAGE_CODE
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    breadcrumbs = [
        {'url': '/', 'name': _('Home'), 'active': True},
    ]
    header = {
        'pt': Helpers.objects.get(id=1).start_page_header_pt,
        'en': Helpers.objects.get(id=1).start_page_header_gb,
        'de': Helpers.objects.get(id=1).start_page_header_de
    }
    tour_header = {
        'pt': Helpers.objects.get(id=1).tour_header_name_PT,
        'en': Helpers.objects.get(id=1).tour_header_name_EN,
        'de': Helpers.objects.get(id=1).tour_header_name_DE
    }
    offer_header = {
        'pt': Helpers.objects.get(id=1).offer_header_name_PT,
        'en': Helpers.objects.get(id=1).offer_header_name_EN,
        'de': Helpers.objects.get(id=1).offer_header_name_DE
    }
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if request.method == 'GET':
        form = BookNow()
    else:
        form = BookNow(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            message = form.cleaned_data['message']
            subject = 'BOOK REQUEST from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')

    context = {
        'contact_me': contact_me,
        'form': form,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'audio': Helpers.objects.get(id=1).audio,
        'company': get_company(),
        'header': header[lang],
        'value': _('Send'),
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'section': {
            'tour_header': tour_header[lang],
            'offer_header': offer_header[lang]
        },
        'img1': Helpers.objects.get(id=1).img,
        'img2': Helpers.objects.get(id=1).img2,
        'img3': Helpers.objects.get(id=1).img3,
        'img4': Helpers.objects.get(id=1).img4,
        'img5': Helpers.objects.get(id=1).img5,
        'lang': lang,
        'offer_list': Offer.objects.all(),
        'tour_list': Tour.objects.all(),
        'breadcrumbs': breadcrumbs

    }
    return render(request, 'partials/home.html', context)


def about(request):
    lang = request.LANGUAGE_CODE
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('About'), 'active': True}
    ]
    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': _('About'),
        'breadcrumbs': breadcrumbs,
        'about_list': About.objects.all(),
        'contact_me': contact_me
    }

    return render(request, 'partials/about.html', context)


def login_or_register(request):
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': True}]
    return render(request, 'partials/login_or_register.html', {'breadcrumbs': breadcrumbs, 'contact_me': contact_me})


def email_me(request):
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')

    context = {
        'contact_me': contact_me,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'form': contact_me,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'title': 'Contact me',
        'company': get_company(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
        ]}
    return render(request, 'partials/email.html', context)


def contact_us(request):
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')

    context = {
        'value': _('SEND'),
        'contact_me': contact_me
    }

    return render(request, 'templates/_contact_us_form.html', context)


def book_form(request):
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    if request.method == 'GET':
        form = BookNow()
    else:
        form = BookNow(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            message = form.cleaned_data['message']
            subject = 'BOOK REQUEST from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')

    context = {
        'contact_me': contact_me,
        'form_book_now': form,
        'value': _('book now')
    }

    return render(request, 'templates/_book_now.html', context)
