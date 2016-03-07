from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Gallery
from .forms import GalleryForm


def gallery_list(request):
    queryset_list = Gallery.objects.all()
    breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/tours', 'name': 'Tours'}]
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
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

        'object_list': queryset,
        'title': 'Gallery',
        'breadcrumbs_list': breadcrumbs_list,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/gallery.html', context)


def gallery_detail(request, pk=None):
    gallery = Gallery.objects.get(pk=pk)
    breadcrumbs_list = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '/contacts', 'name': 'Contacts', 'active': False},
        ]
    context = {
        'breadcrumbs_list': breadcrumbs_list,
        # 'title': gallery.first_name + ' ' + gallery.last_name,
        'object': gallery,
    }

    return render(request, 'partials/detail.html', context)


def gallery_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = GalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Contact Created')
            return redirect('gallery:list')

        context = {
            'title': 'Contact creating',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/contacts', 'name': 'Contacts', 'active': False},
                {'url': '#', 'name': 'Contact creating', 'active': True}],
            'value': 'Contact creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def gallery_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Gallery, pk=pk)
        breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/contacts', 'name': 'Contacts'},
                            {'url': '#', 'name': instance.first_name + ' ' + instance.last_name, 'active': True}]
        form = GalleryForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Contact saved')
            return redirect('gallery:list')

        context = {
            'title': 'Contact Edit',
            'breadcrumbs_list': breadcrumbs_list,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def gallery_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Gallery, pk=pk)
    instance.delete()
    messages.success(request, 'Contact deleted')
    return redirect('gallery:list')


