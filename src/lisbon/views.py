from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from offer.models import Offer
from tours.models import About
from helpers.models import Helpers


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def home(request):
    lang = request.LANGUAGE_CODE
    breadcrumbs = [
        {'url': '/', 'name': _('Home'), 'active': True},
    ]
    header = {
        'pt': Helpers.objects.get(id=1).start_page_header_pt,
        'en': Helpers.objects.get(id=1).start_page_header_gb,
        'de': Helpers.objects.get(id=1).start_page_header_de
    }
    context = {
        'audio': Helpers.objects.get(id=1).audio,
        'company': get_company(),
        'header': header[lang],
        'img1': Helpers.objects.get(id=1).img,
        'img2': Helpers.objects.get(id=1).img2,
        'img3': Helpers.objects.get(id=1).img3,
        'lang': lang,
        'object_list': Offer.objects.all(),
        'breadcrumbs': breadcrumbs

    }
    return render(request, 'partials/home.html', context)


def about(request):
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('About'), 'active': True}
    ]
    context = {
        'company': get_company(),
        'title': _('About'),
        'breadcrumbs': breadcrumbs,
        'about_list': About.objects.all()
    }

    return render(request, 'partials/about.html', context)


def login_or_register(request):
    breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': True}]
    return render(request, 'partials/login_or_register.html', {'breadcrumbs': breadcrumbs})
