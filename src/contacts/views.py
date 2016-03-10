from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
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


def contact_list(request):
    queryset_list = Contact.objects.all()
    lang = get_lang(request)
    navbar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': '#', 'name': navbar[lang].contact, 'active': True}
    ]
    path = request.get_full_path()
    gb = path.replace(lang, 'gb')
    pt = path.replace(lang, 'pt')
    de = path.replace(lang, 'de')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
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
        'title': navbar[lang].contact,
        'breadcrumbs_list': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/contact.html', context)


def contact_detail(request, pk=None):
    contact = Contact.objects.get(pk=pk)
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

    breadcrumbs = [
        {'url': '/', 'name': navbar[lang].home},
        {'url': path.replace(pk + '/', ''), 'name': navbar[lang].contact},
        {'url': '#', 'name': contact.first_name + ' ' + contact.last_name, 'active': True}
    ]

    context = {
        'pt': pt,
        'de': de,
        'gb': gb,
        'lang': lang,
        'nav': navbar[lang],
        'title': contact.first_name + ' ' + contact.last_name,
        'breadcrumbs_list': breadcrumbs,
        'contact': contact,
    }

    return render(request, 'templates/_contact_details.html', context)


def contact_create(request):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Contact Created')
            return redirect('contact:list')

        context = {
            'lang': lang,
            'title': 'Contact creating',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/contacts', 'name': 'Contacts', 'active': False},
                {'url': '#', 'name': 'Contact creating', 'active': True}],
            'value': 'Contact creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def contact_update(request, pk=None):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Contact, pk=pk)
        breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/contacts', 'name': 'Contacts'},
                            {'url': '#', 'name': instance.first_name + ' ' + instance.last_name, 'active': True}]
        form = ContactForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Contact saved')
            return redirect('contact:list')

        context = {
            'lang': lang,
            'title': 'Contact Edit',
            'breadcrumbs_list': breadcrumbs_list,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def contact_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Contact, pk=pk)
    instance.delete()
    messages.success(request, 'Contact deleted')
    return redirect('contact:list')
