from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from helpers.models import PTNavigation, GBNavigation, DENavigation

from .models import Gallery
from .forms import GalleryForm


def get_lang(request):
    lang = request.path
    if 'pt' in lang:
        return 'pt'
    else:
        if 'gb' in lang:
            return 'gb'
        else:
            return 'de'


def gallery_list(request):
    queryset_list = Gallery.objects.all()
    lang = get_lang(request)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': '#', 'name': navbar[lang].gallery, 'active': True}
    ]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
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
        'title': navbar[lang].gallery,
        'breadcrumbs_list': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/gallery.html', context)


def gallery_detail(request, pk=None):
    lang = get_lang(request)
    gallery = Gallery.objects.get(pk=pk)
    breadcrumbs = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '/gallery', 'name': 'Gallery', 'active': False},
        {'url': '#', 'name': gallery.title, 'active': True},
    ]
    context = {
        'lang': lang,
        'breadcrumbs_list': breadcrumbs,
        'title': gallery.title,
        'object': gallery,
    }

    return render(request, 'templates/_gallery_details.html', context)


def gallery_create(request):
    lang = get_lang(request)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': '#', 'name': navbar[lang].gallery},
        {'url': '#', 'name': 'Create Gallery', 'active': True}
    ]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = GalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Gallery Created')
            return redirect('gallery:list')

        context = {
            'pt': pt,
            'de': de,
            'gb': gb,
            'lang': lang,
            'nav': navbar[lang],
            'title': 'Create Gallery',
            'breadcrumbs_list': breadcrumbs,
            'value': 'Contact creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def gallery_update(request, pk=None):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Gallery, pk=pk)
        breadcrumbs = [
            {'url': '/', 'name': 'Home', 'active': False},
            {'url': '/gallery', 'name': 'Gallery', 'active': False},
            {'url': '#', 'name': instance.title, 'active': True}]
        form = GalleryForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Gallery saved')
            return redirect('gallery:list')

        context = {
            'lang': lang,
            'title': 'Contact Edit',
            'breadcrumbs_list': breadcrumbs,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def gallery_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Gallery, pk=pk)
    instance.delete()
    messages.success(request, 'Gallery deleted')
    return redirect('gallery:list')
