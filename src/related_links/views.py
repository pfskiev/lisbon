from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from tours.models import Category
from helpers.models import Helpers
from tours.forms import ContactMe
from offer.models import OfferCategory
from .models import RelatedLink
from .forms import RelatedLinkForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def related_links_list(request):
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = RelatedLink.objects.all()
    lang = get_lang(request)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Related links'), 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        if 'pt' in lang:
            queryset_list = queryset_list.filter(
                Q(title_PT__icontains=query) |
                Q(description_PT__icontains=query)
            ).distinct()
        else:
            if 'en' in lang:
                queryset_list = queryset_list.filter(
                    Q(title_EN__icontains=query) |
                    Q(description_EN__icontains=query)
                ).distinct()
            else:
                if 'de' in lang:
                    queryset_list = queryset_list.filter(
                        Q(title_DE__icontains=query) |
                        Q(description_DE__icontains=query))

    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

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
        'title': _('Related links'),
        'object_list': queryset,
        'breadcrumbs': breadcrumbs,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'partials/related-links.html', context)


def related_links_detail(request, pk=None):
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    related_link = RelatedLink.objects.get(pk=pk)
    lang = get_lang(request)
    title = {
        'pt': related_link.title_PT,
        'en': related_link.title_EN,
        'de': related_link.title_DE
    }
    description = {
        'pt': related_link.description_PT,
        'en': related_link.description_EN,
        'de': related_link.description_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home'), 'active': False},
        {'url': '/related-links', 'name': _('Related links'), 'active': False},
        {'url': '#', 'name': title[lang], 'active': True}]

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
        'breadcrumbs': breadcrumbs,
        'title': title[get_lang(request)],
        'object': {
            'id': related_link.id,
            'keywords_SEO': related_link.keywords_SEO,
            'description_SEO': related_link.description_SEO,
            'title': title[lang],
            'description': description[lang],
            'img': related_link.img,
        },
    }

    return render(request, 'templates/_related_links_details.html', context)


def related_links_create(request):
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = RelatedLinkForm(request.POST or None, request.FILES or None)
        breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': False},
                       {'url': '/related-links', 'name': _('Related links'),
                        'active': False},
                       {'url': '#', 'name': _('Create Offer'), 'active': True}]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Link Created')
            return redirect('related_links:list')

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
        'title': _('Create Offer'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'templates/_form.html', context)


def related_links_update(request, pk=None):
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        related_link = get_object_or_404(RelatedLink, pk=pk)
        lang = get_lang(request)
        title = {
            'pt': related_link.title_PT,
            'en': related_link.title_EN,
            'de': related_link.title_DE
        }
        breadcrumbs = [{'url': '/', 'name': _('Home')},
                       {'url': '/related-links', 'name': _('Related links')},
                       {'url': '#', 'name': _('Edit') + ' ' + title[lang], 'active': True}]
        form = RelatedLinkForm(request.POST or None, request.FILES or None, instance=related_link)
        if form.is_valid():
            related_link = form.save(commit=False)
            related_link.save()
            messages.success(request, _('Link saved'))
            return redirect('related_links:list')

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
            'title': _('Edit') + ' ' + title[lang],
            'breadcrumbs': breadcrumbs,
            'instance': related_link,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def related_links_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(RelatedLink, pk=pk)
    instance.delete()
    messages.success(request, 'Link deleted')
    return redirect('related_links:list')
