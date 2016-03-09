import string

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from helpers.models import PTNavigation, GBNavigation, DENavigation
from .forms import TourForm
from .models import Tour


def get_lang(request):
    lang = request.get_full_path()
    if 'pt' in lang:
        return 'pt'
    else:
        if 'gb' in lang:
            return 'gb'
        else:
            return 'de'


def tour_list(request):
    queryset_list = Tour.objects.all()
    lang = get_lang(request)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': '#', 'name': navbar[lang].tours, 'active': True}
    ]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(description_pt__icontains=query)
        ).distinct()
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
        'pt': pt,
        'de': de,
        'gb': gb,
        'lang': lang,
        'nav': navbar[lang],
        'title': navbar[lang].tours,
        'breadcrumbs_list': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/tours.html', context)


def tour_detail(request, pk=None):
    tour = Tour.objects.get(pk=pk)
    lang = get_lang(request)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')

    tour_title = {
        'pt': tour.title_pt,
        'gb': tour.title_gb,
        'de': tour.title_de
    }
    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': path.replace(pk + '/', ''), 'name': navbar[lang].tours},
        {'url': '#', 'name': tour_title[lang], 'active': True}
    ]

    context = {
        'pt': pt,
        'de': de,
        'gb': gb,
        'lang': lang,
        'nav': navbar[lang],
        'title': tour_title[lang],
        'breadcrumbs_list': breadcrumbs,
        'object': tour,
    }

    return render(request, 'partials/detail.html', context)


def tour_update(request, pk=None):
    lang = get_lang(request)
    tour = Tour.objects.get(pk=pk)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')

    tour_title = {
        'pt': tour.title_pt,
        'gb': tour.title_gb,
        'de': tour.title_de
    }
    breadcrumbs_list = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': path.replace(pk + '/', ''), 'name': navbar[lang].tours},
        {'url': '#', 'name': tour_title[lang], 'active': True}
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
            return redirect('tour_list')

        context = {
            'pt': pt,
            'de': de,
            'gb': gb,
            'lang': lang,
            'nav': navbar[lang],
            'title': tour_title[lang] + ' edit',
            'breadcrumbs_list': breadcrumbs_list,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def tour_create(request):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = TourForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully Created')
            return redirect('tour_gb:list')

        context = {
            'lang': lang,
            'title': 'Tour create',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home'},
                {'url': '#', 'name': 'Tour create', 'active': True}
            ],
            'value': 'Create Tour',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def tour_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Tour, pk=pk)
    instance.delete()
    messages.success(request, 'Tour deleted')
    return redirect('tour_gb:list')
