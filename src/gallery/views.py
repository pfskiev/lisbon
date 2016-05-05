from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from helpers.models import Helpers
from tours.models import Category
from .models import Gallery
from .forms import GalleryForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def gallery_list(request):
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    lang = get_lang(request)
    queryset_list = Gallery.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Gallery'), 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        if 'pt' in lang:
            queryset_list = queryset_list.filter(
                Q(title_PT__icontains=query) |
                Q(description_PT__icontains=query)
                # Q(category__category__icontains=query)
            ).distinct()
        else:
            if 'en' in lang:
                queryset_list = queryset_list.filter(
                    Q(title_EN__icontains=query) |
                    Q(description_EN__icontains=query)
                    # Q(category__category__icontains=query)
                ).distinct()
            else:
                if 'de' in lang:
                    queryset_list = queryset_list.filter(
                        Q(title_DE__icontains=query) |
                        Q(description_DE__icontains=query)
                        # Q(category__category__icontains=query)
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
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'title': _('Gallery'),
        'breadcrumbs': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/gallery.html', context)


def gallery_detail(request, pk=None):
    gallery = Gallery.objects.get(pk=pk)
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    gallery_title = {
        'pt': gallery.title_PT,
        'en': gallery.title_EN,
        'de': gallery.title_DE
    }
    gallery_description = {
        'pt': gallery.description_PT,
        'en': gallery.description_EN,
        'de': gallery.description_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '/gallery', 'name': _('Gallery')},
        {'url': '#', 'name': gallery_title[lang], 'active': True}
    ]
    gallery_current = {
        'title': gallery_title[lang],
        'description': gallery_description[lang],
        'id': gallery.id,
        'video': gallery.video,
        'img': gallery.img,
        'img1': gallery.img_1,
        'img2': gallery.img_2,
        'img3': gallery.img_3,
    }
    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'breadcrumbs': breadcrumbs,
        'title': gallery_title[lang],
        'object': gallery_current,
    }

    return render(request, 'templates/_gallery_details.html', context)


def gallery_update(request, pk=None):
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        gallery = get_object_or_404(Gallery, pk=pk)
        lang = get_lang(request)
        gallery_title = {
            'pt': gallery.title_PT,
            'en': gallery.title_EN,
            'de': gallery.title_DE
        }
        breadcrumbs = [
            {'url': '/', 'name': _('Home')},
            {'url': '/gallery', 'name': _('Gallery')},
            {'url': '#', 'name': gallery_title[lang], 'active': True}
        ]
        form = GalleryForm(request.POST or None, request.FILES or None, instance=gallery)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.save()
            messages.success(request, _('Gallery edited'))
            return redirect('gallery:list')

        context = {
            'footer': {
                'about': footer[lang],
                'icon': Helpers.objects.get(id=1).footer_icon
            },
            'categories_list': Category.objects.all(),
            'company': get_company(),
            'title': _('Gallery edit'),
            'breadcrumbs': breadcrumbs,
            'instance': gallery,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def gallery_create(request):
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = GalleryForm(request.POST or None, request.FILES or None)
        breadcrumbs = [
            {'url': '/', 'name': _('Home')},
            {'url': '/gallery', 'name': _('Gallery')},
            {'url': '#', 'name': _('Create Gallery'), 'active': True}
        ]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, _('Gallery created'))
            return redirect('gallery:list')

        context = {
            'footer': {
                'about': footer[lang],
                'icon': Helpers.objects.get(id=1).footer_icon
            },
            'categories_list': Category.objects.all(),
            'company': get_company(),
            'title': _('Create Gallery'),
            'breadcrumbs': breadcrumbs,
            'value': _('Add'),
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def gallery_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Gallery, pk=pk)
    instance.delete()
    messages.success(request, _('Gallery deleted'))
    return redirect('gallery:list')
