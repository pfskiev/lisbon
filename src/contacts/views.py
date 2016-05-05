from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from helpers.models import Helpers
from tours.models import Category
from .models import Contact, ContactHelpers
from .forms import ContactForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def contact_list(request):
    lang = get_lang(request)
    queryset_list = Contact.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Contacts'), 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, ContactHelpers.objects.get(id=1).pagination)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    context = {
        'footer': {
            'about': footer[lang]
        },
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'title': _('Contacts'),
        'breadcrumbs': breadcrumbs,
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/contact.html', context)


def contact_detail(request, pk=None):
    lang = get_lang(request)
    contact = Contact.objects.get(pk=pk)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '/contacts', 'name': _('Contacts')},
        {'url': '#', 'name': contact.first_name + ' ' + contact.last_name, 'active': True}
    ]
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    context = {
        'footer': {
            'about': footer[lang]
        },
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'title': contact.first_name + ' ' + contact.last_name,
        'breadcrumbs': breadcrumbs,
        'object': contact,
    }

    return render(request, 'templates/_contact_details.html', context)


def contact_create(request):
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
        breadcrumbs = [
            {'url': '/', 'name': _('Home')},
            {'url': '/contacts', 'name': _('Contacts')},
            {'url': '#', 'name': _('Create Contact'), 'active': True}
        ]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, _('Contact Created'))
            return redirect('contact:list')

        context = {
            'footer': {
                'about': footer[lang]
            },
            'categories_list': Category.objects.all(),
            'company': get_company(),
            'title': _('Create Contact'),
            'breadcrumbs': breadcrumbs,
            'value': _('Add'),
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def contact_update(request, pk=None):
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        contact = get_object_or_404(Contact, pk=pk)
        breadcrumbs = [
            {'url': '/', 'name': _('Home')},
            {'url': '/contacts', 'name': _('Contacts')},
            {'url': '#', 'name': contact.first_name + ' ' + contact.last_name, 'active': True}
        ]
        form = ContactForm(request.POST or None, request.FILES or None, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, _('Contact saved'))
            return redirect('contact:list')

        context = {
            'footer': {
                'about': footer[lang]
            },
            'categories_list': Category.objects.all(),
            'company': get_company(),
            'title': _('Contact Edit'),
            'breadcrumbs': breadcrumbs,
            'instance': contact,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def contact_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Contact, pk=pk)
    instance.delete()
    messages.success(request, _('Contact deleted'))
    return redirect('contact:list')
