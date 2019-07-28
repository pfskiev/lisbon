from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from helpers.models import Helpers
from tours.forms import BookNow
from tours.models import Category
from tours.models import Tour


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def category_list(request, slug=None):
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Tour.objects.filter(category__url__contains=slug)
    lang = get_lang(request)
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
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
    booking_form = BookNow()
    context = {
        'booking_form': booking_form,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'categories_list': Category.objects.all(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
            {'url': '/', 'name': _('Tours')},
            {'url': '#', 'name': category[0], 'active': True}
        ],
        'title': _('category'),
        'object_list': queryset,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'templates/_tour_cat.html', context)
