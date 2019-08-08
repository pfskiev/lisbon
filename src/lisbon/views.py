from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from helpers.models import Helpers
from offer.models import Offer
from offer.models import OfferCategory
from tours.forms import BookNow
from tours.models import Category, Tour, About


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def home(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    booking_form = BookNow()

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
    context = {
        'booking_form': booking_form,
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
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)

    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('About'), 'active': True}
    ]
    lang = request.LANGUAGE_CODE
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
    }

    return render(request, 'partials/about.html', context)


def login_or_register(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)

    breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': True}]
    return render(request, 'partials/login_or_register.html', {'breadcrumbs': breadcrumbs})


def search(request):
    lang = request.LANGUAGE_CODE

    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }

    offer_queryset = Offer.objects.all()
    tour_queryset = Tour.objects.all()
    query = request.GET.get('q')
    offer_object_list = []
    tour_object_list = []

    if 'pt' in lang:
        offer_object_list = offer_queryset.filter(
            Q(title_PT__icontains=query) |
            Q(description_PT__icontains=query)
        ).distinct()
    else:
        if 'en' in lang:
            offer_object_list = offer_queryset.filter(
                Q(title_EN__icontains=query) |
                Q(description_EN__icontains=query)
            ).distinct()
        else:
            if 'de' in lang:
                offer_object_list = offer_queryset.filter(
                    Q(title_DE__icontains=query) |
                    Q(description_DE__icontains=query))

    if 'pt' in lang:
        tour_object_list = tour_queryset.filter(
            Q(title_PT__icontains=query) |
            Q(description_PT__icontains=query)
        ).distinct()
    else:
        if 'en' in lang:
            tour_object_list = tour_queryset.filter(
                Q(title_EN__icontains=query) |
                Q(description_EN__icontains=query)
            ).distinct()
        else:
            if 'de' in lang:
                tour_object_list = tour_queryset.filter(
                    Q(title_DE__icontains=query) |
                    Q(description_DE__icontains=query))

    context = {
        'offer_object_list': offer_object_list,
        'tour_object_list': tour_object_list,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'title': 'Contact me',
        'company': get_company(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
        ]}
    return render(request, 'partials/search.html', context)


def contact_us(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)

    context = {
        'value': _('SEND'),
    }

    return render(request, 'templates/_contact_us_form.html', context)


def book_form(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)

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
        'form_book_now': form,
        'value': _('book now')
    }

    return render(request, 'templates/_book_now.html', context)
