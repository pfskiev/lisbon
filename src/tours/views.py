from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from helpers.models import Helpers
from offer.models import OfferCategory
from .forms import TourForm, BookNow
from .models import Tour, Category


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def tour_list(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Tour.objects.all()
    lang = get_lang(request)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Tours'), 'active': True},
    ]
    query = request.GET.get('q')
    if query:
        if 'pt' in lang:
            queryset_list = queryset_list.filter(
                Q(title_PT__icontains=query) |
                Q(description_PT__icontains=query) |
                Q(category__category__icontains=query)
            ).distinct()
        else:
            if 'en' in lang:
                queryset_list = queryset_list.filter(
                    Q(title_EN__icontains=query) |
                    Q(description_EN__icontains=query) |
                    Q(category__category__icontains=query)
                ).distinct()
            else:
                if 'de' in lang:
                    queryset_list = queryset_list.filter(
                        Q(title_DE__icontains=query) |
                        Q(description_DE__icontains=query) |
                        Q(category__category__icontains=query)
                    )
    paginator = Paginator(queryset_list, 12)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    booking_form = BookNow()

    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'booking_form': booking_form,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': _('Tours'),
        'breadcrumbs': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/tours.html', context)


def tour_detail(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    booking_form = BookNow()
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    tour = Tour.objects.get(pk=pk)

    title = {
        'pt': tour.title_PT,
        'en': tour.title_EN,
        'de': tour.title_DE
    }
    description = {
        'pt': tour.description_PT,
        'en': tour.description_EN,
        'de': tour.description_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '/', 'name': _('Tours')},
        {'url': '/', 'name': title[lang], 'active': True},
    ]
    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'booking_form': booking_form,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': title[lang],
        'breadcrumbs': breadcrumbs,
        'object': {
            'keywords_SEO': tour.keywords_SEO,
            'description_SEO': tour.description_SEO,
            'price': tour.price,
            'title': title[lang],
            'id': tour.id,
            'img': tour.img,
            'url': tour.url,
            'description': description[lang],
        },
    }
    return render(request, 'partials/detail.html', context)


def tour_update(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    tour = Tour.objects.get(pk=pk)
    tour_title = {
        'pt': tour.title_PT,
        'en': tour.title_EN,
        'de': tour.title_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '/tours', 'name': _('Tours')},
        {'url': '#', 'name': tour_title[lang], 'active': True},
    ]

    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Tour, pk=pk)
        form = TourForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Tour saved')
            return redirect('tour:list')

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
            'title': _('Edit') + ' ' + tour_title[lang],
            'breadcrumbs': breadcrumbs,
            'instance': instance,
            'form': form,
            'value': _('Add')
        }
        return render(request, 'templates/_form.html', context)


def tour_create(request):
    lang = request.LANGUAGE_CODE
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
                      {'url': '/', 'name': _('Tours')},
                      {'url': '#', 'name': _('Create Tour'), 'active': True},
                  ],
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = TourForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully Created')
            return redirect('tour:list')

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
        'lang': lang,
        'title': 'Tour create',
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'templates/_form.html', context)


def tour_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Tour, pk=pk)
    instance.delete()
    messages.success(request, 'Tour deleted')
    return redirect('tour:list')


def tour_category(request, slug=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }

    queryset_list = Tour.objects.filter(category__url__contains=slug)
    paginator = Paginator(queryset_list, 6)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    category = Category.objects.filter(url__icontains=slug)
    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'booking_form ': BookNow(),
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
            {'url': '/tours', 'name': _('Tours')},
            {'url': '#', 'name': category[0], 'active': True}
        ],
        'title': category[0],  # _('category'),
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'templates/_tour_cat.html', context)


def tour_success(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'title': 'Thank you very much for your contact. We will get in touch with you soon!',
        'company': get_company(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
        ]}

    return render(request, 'partials/success.html', context)


def tour_fail(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }

    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'title': 'Sorry, something goes wrong! Please try again.',
        'company': get_company(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
        ]}
    return render(request, 'partials/fail.html', context)
