from django.shortcuts import render
from offer.models import Offer
from tours.models import About
from helpers.models import PTNavigation, GBNavigation, DENavigation


def get_lang(request):
    lang = request.get_full_path()
    if 'pt' in lang:
        return 'pt'
    else:
        if 'gb' in lang:
            return 'gb'
        else:
            return 'de'


def home(request):
    lang = get_lang(request)
    nav_bar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs_list = [
        {'url': '/', 'name': nav_bar[lang].home, 'active': True},
        ]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    context = {
        'pt': pt,
        'de': de,
        'gb': gb,
        'lang': lang,
        'nav': nav_bar[lang],
        'offer_list': Offer.objects.all(),
        'breadcrumbs_list': breadcrumbs_list
    }

    return render(request, 'partials/home.html', context)


def about(request):
    lang = get_lang(request)
    nav_bar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs_list = [
        {'url': '/', 'name': nav_bar[lang].home},
        {'url': '#', 'name': nav_bar[lang].about, 'active': True}]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    context = {
        'lang': lang,
        'nav': nav_bar[lang],
        'pt': pt,
        'de': de,
        'gb': gb,
        'title': nav_bar[lang].about,
        'breadcrumbs_list': breadcrumbs_list,
        'about_list': About.objects.all()
    }

    return render(request, 'partials/about.html', context)


def login_or_register(request):
    lang = get_lang(request)
    nav_bar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs_list = [
        {'url': '/', 'name': nav_bar[lang].home},
        {'url': '#', 'name': nav_bar[lang].review, 'active': True}]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    context = {
        'lang': lang,
        'nav': nav_bar[lang],
        'pt': pt,
        'de': de,
        'gb': gb,
        'breadcrumbs_list': breadcrumbs_list,

    }
    return render(request, 'partials/login_or_register.html', context)


