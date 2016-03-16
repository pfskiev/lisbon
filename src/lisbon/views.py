from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from offer.models import Offer
from tours.models import About
from helpers.models import Helpers
from tours.models import Category, Tour

from tours.forms import BookNow


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def home(request):
    lang = request.LANGUAGE_CODE
    if request.method == 'GET':
        form = BookNow()
    else:
        form = BookNow(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            subject = 'BOOK REQUEST from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = ['podlesny@outlook.com']
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
                # send_mail('Subject here', message, settings.EMAIL_HOST_USER,
                #           ['podlesny@outlook.com'], fail_silently=True)
                # send_mail(subject=fullname, body=phone, message, ['podlesny@outlook.com'])
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
    context = {
        'form': form,
        'categories_list': Category.objects.all(),
        'audio': Helpers.objects.get(id=1).audio,
        'company': get_company(),
        'header': header[lang],
        'img1': Helpers.objects.get(id=1).img,
        'img2': Helpers.objects.get(id=1).img2,
        'img3': Helpers.objects.get(id=1).img3,
        'lang': lang,
        'object_list': Offer.objects.all(),
        'tour_list': Tour.objects.all(),
        'breadcrumbs': breadcrumbs

    }
    return render(request, 'partials/home.html', context)


def about(request):
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('About'), 'active': True}
    ]
    context = {
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'title': _('About'),
        'breadcrumbs': breadcrumbs,
        'about_list': About.objects.all()
    }

    return render(request, 'partials/about.html', context)


def login_or_register(request):
    breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': True}]
    return render(request, 'partials/login_or_register.html', {'breadcrumbs': breadcrumbs})
