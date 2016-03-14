from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from .models import Tour, Category
from .forms import TourForm
from helpers.models import Helpers


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def tour_list(request):
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
                Q(description_PT__icontains=query)
                # Q(category__icontains=query)
            ).distinct()
        else:
            if 'en' in lang:
                queryset_list = queryset_list.filter(
                    Q(title_EN__icontains=query) |
                    Q(description_EN__icontains=query)
                    # Q(category__icontains=query)
                ).distinct()
            else:
                if 'de' in lang:
                    queryset_list = queryset_list.filter(
                        Q(title_DE__icontains=query) |
                        Q(description_DE__icontains=query)
                        # Q(category__icontains=query)
                    )
    paginator = Paginator(queryset_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'company': get_company(),
        'title': _('Tours'),
        'breadcrumbs': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/tours.html', context)


def tour_detail(request, pk=None):
    tour = Tour.objects.get(pk=pk)
    lang = get_lang(request)
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
        'company': get_company(),
        'title': title[lang],
        'breadcrumbs': breadcrumbs,
        'object': {
            'keywords': tour.keywords_SEO,
            'description_SEO': tour.description_SEO,
            'title': title[lang],
            'id': tour.id,
            'img': tour.img,
            'url': tour.url,
            'description': description[lang],
        },
    }
    return render(request, 'partials/detail.html', context)


def tour_update(request, pk=None):
    lang = get_lang(request)
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
            'company': get_company(),
            'title': _('Edit') + ' ' + tour_title[lang],
            'breadcrumbs': breadcrumbs,
            'instance': instance,
            'form': form,
            'value': _('Add')
        }
        return render(request, 'templates/_form.html', context)


def tour_create(request):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = TourForm(request.POST or None, request.FILES or None)
        breadcrumbs = [
                          {'url': '/', 'name': 'Home'},
                          {'url': '/', 'name': _('Tours')},
                          {'url': '/', 'name': _('Create Tour'), 'active': True},
                      ],
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully Created')
            return redirect('tour:list')

        context = {
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


# def tour_category(request):
#     tours = Tour.objects.all()
#     tours.filter(category__icontains='king')
#
#     context = {
#         'object_list': tours
#     }
#
#     return render(request, 'templates/_tour_cat.html', context)
