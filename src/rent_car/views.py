from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.views.generic import View
from tours.models import Category
from tours.forms import ContactMe
from offer.models import OfferCategory
from helpers.models import Helpers
from .models import Car, CarCategory
from .forms import CarForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def rent_car_list(request):
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
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Car Rent in Lisbon'), 'active': True}
    ]
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Car.objects.all()
    lang = get_lang(request)
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
        'contact_me': contact_me,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': _('Car Rent in Lisbon'),
        'object_list': queryset,
        'breadcrumbs': breadcrumbs,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'partials/rent-car.html', context)


def rent_car_detail(request, pk=None):
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
    car = Car.objects.get(pk=pk)
    lang = get_lang(request)
    title = {
        'pt': car.title_PT,
        'en': car.title_EN,
        'de': car.title_DE
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
        'object': car,
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'offer': Car.objects.get(pk=pk)
    }

    return render(request, 'templates/_offer_details.html', context)


def rent_car_create(request):
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
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = CarForm(request.POST or None, request.FILES or None)
        breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': False},
                       {'url': '/offer', 'name': _('Rent Car'), 'active': False},
                       {'url': '#', 'name': _('Create Car'), 'active': True}]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Car Created')
            return redirect('rent_car:list')

    context = {
        'contact_me': contact_me,
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'company': get_company(),
        'title': _('Create Car'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'templates/_form.html', context)


def rent_car_update(request, pk=None):
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
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        car = get_object_or_404(Car, pk=pk)
        lang = get_lang(request)
        title = {
            'pt': car.title_PT,
            'en': car.title_EN,
            'de': car.title_DE
        }
        breadcrumbs = [{'url': '/', 'name': _('Home')},
                       {'url': '/offer', 'name': _('Rent Car')},
                       {'url': '#', 'name': _('Edit') + ' ' + title[lang], 'active': True}]
        form = CarForm(request.POST or None, request.FILES or None, instance=car)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            messages.success(request, _('Car saved'))
            return redirect('rent_car:list')

        context = {
            'contact_me': contact_me,
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
            'instance': car,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def rent_car_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Car, pk=pk)
    instance.delete()
    messages.success(request, 'Car deleted')
    return redirect('rent_car:list')


def rent_car_category(request, slug=None):
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
    queryset_list = Car.objects.filter(category__slug__contains=slug)
    lang = get_lang(request)
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
                        Q(description_DE__icontains=query)
                    ).distinct()
    paginator = Paginator(queryset_list, 6)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    category = CarCategory.objects.filter(slug__icontains=slug)

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

    return render(request, 'templates/_car_category.html', context)

