from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from .models import Offer, OfferCategory
from .forms import OfferForm
from tours.models import Category
from helpers.models import Helpers
from tours.forms import ContactMe


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def offer_list(request):
    # if request.method == 'GET':
    #     contact_me = ContactMe()
    # else:
    #     contact_me = ContactMe(request.POST)
    #     if contact_me.is_valid():
    #         fullname = contact_me.cleaned_data['fullname']
    #         message = contact_me.cleaned_data['message']
    #         subject = 'Mail from ' + fullname
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = settings.EMAIL_TO
    #         try:
    #             send_mail(subject, message, from_email, to_list, fail_silently=False)
    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #         return redirect('tour:success')
    #     else:
    #         return redirect('tour:fail')
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Offer.objects.all()
    lang = get_lang(request)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Offers'), 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)

    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    # if not request.user.is_staff or not request.user.is_superuser:
    #     return redirect('accounts:signup')
    # else:
    #

    form = OfferForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Offer Created')
        return redirect('offer:list')

    context = {
        # 'contact_me': contact_me,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': _('Offers'),
        'object_list': queryset,
        'breadcrumbs': breadcrumbs,
        'page_request_var': page_request_var,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'partials/offer.html', context)


def offer_detail(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')

    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    offer = Offer.objects.get(pk=pk)
    lang = get_lang(request)
    title = {
        'pt': offer.title_PT,
        'en': offer.title_EN,
        'de': offer.title_DE
    }
    breadcrumbs = [
        {'url': '/', 'name': _('Home'), 'active': False},
        {'url': '/offer', 'name': _('Offers'), 'active': False},
        {'url': '#', 'name': title[lang], 'active': True}]
    context = {
        'contact_me': contact_me,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'company': get_company(),
        'breadcrumbs': breadcrumbs,
        'title': title[get_lang(request)],
        'object': offer,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'offer': Offer.objects.get(pk=pk)
    }

    return render(request, 'templates/_offer_details.html', context)


def offer_create(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = OfferForm(request.POST or None, request.FILES or None)
        breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': False},
                       {'url': '/offer', 'name': _('Offers'), 'active': False},
                       {'url': '#', 'name': _('Create Offer'), 'active': True}]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Offer Created')
            return redirect('offer:list')

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


def offer_update(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        offer = get_object_or_404(Offer, pk=pk)
        lang = get_lang(request)
        title = {
            'pt': offer.title_PT,
            'en': offer.title_EN,
            'de': offer.title_DE
        }
        breadcrumbs = [{'url': '/', 'name': _('Home')},
                       {'url': '/offer', 'name': _('Offers')},
                       {'url': '#', 'name': _('Edit') + ' ' + title[lang], 'active': True}]
        form = OfferForm(request.POST or None, request.FILES or None, instance=offer)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            messages.success(request, _('Offer saved'))
            return redirect('offer:list')

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
            'instance': offer,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def offer_delete(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Offer, pk=pk)
    instance.delete()
    messages.success(request, 'Offer deleted')
    return redirect('offer:list')


def offer_category(request, slug=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    if request.method == 'GET':
        contact_me = ContactMe()
    else:
        contact_me = ContactMe(request.POST)
        if contact_me.is_valid():
            fullname = contact_me.cleaned_data['fullname']
            message = contact_me.cleaned_data['message']
            subject = 'Mail from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:success')
        else:
            return redirect('tour:fail')
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Offer.objects.filter(category__slug__contains=slug)
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

    category = OfferCategory.objects.filter(slug__icontains=slug)

    context = {
        'contact_me': contact_me,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
            {'url': '/tours', 'name': _('Offers')},
            {'url': '#', 'name': category[0], 'active': True}
        ],
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'title': category[0],  # _('category'),
        'object_list': queryset,
        'page_request_var': page_request_var,
    }

    return render(request, 'templates/_offer_category.html', context)
