from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from helpers.models import Helpers
from offer.models import OfferCategory
from tours.models import Category
from .forms import ReviewForm
from .models import Review


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def review_list(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Reviews'), 'active': True}
    ]
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Review.objects.all().order_by('-timestamp')
    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    form = ReviewForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if not request.user.is_authenticated():
            return redirect('login_or_register')
        else:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            message = 'Please check and approve new review: "' + request.POST.get('review', '') \
                      + '" on http://www.goldenlisbon.com/admin/review/review/'
            subject = 'New review!'
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('review:list')

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
        'object_list': queryset,
        'title': _('Reviews'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/review.html', context)


def review_detail(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    review = Review.objects.get(pk=pk)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '/reviews', 'name': _('Reviews')},
        {'url': '#', 'name': review.category.category, 'active': True}
    ]
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
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
        'breadcrumbs': breadcrumbs,
        'title': review.category.category,
        'object': review,
    }

    return render(request, 'templates/_review_details.html', context)


def review_create(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    breadcrumbs = [

                      {'url': '/', 'name': _('Home')},
                      {'url': '/reviews', 'name': _('Review')},
                      {'url': '#', 'name': _('Review creating'), 'active': True}],
    if not request.user.is_authenticated():
        return redirect('login_or_register')
    else:

        form = ReviewForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            message = 'Please check and approve new review: "' + request.POST.get('review', '') \
                      + '" on http://www.goldenlisbon.com/admin/review/review/'
            subject = 'New review!'
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('review:list')

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
            'lang': lang,
            'title': 'Review creating',
            'breadcrumbs': breadcrumbs,
            'value': _('Add'),
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def review_update(request, pk=None):
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
        instance = get_object_or_404(Review, pk=pk)
        breadcrumbs = [
            {'url': '/', 'name': _('Home'), 'active': False},
            {'url': '/reviews', 'name': _('Review'), 'active': False},
            {'url': '#', 'name': instance.title, 'active': True}]
        form = ReviewForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Review saved')
            return redirect('review:list')

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
            'lang': lang,
            'title': 'Review Edit',
            'breadcrumbs': breadcrumbs,
            'instance': instance,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def review_filter(request, slug=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = request.LANGUAGE_CODE
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    category = Category.objects.filter(url__icontains=slug)

    queryset_list = Review.objects.filter(category__category__url__contains=slug)
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(review__icontains=query) |
            Q(user__name__icontains=query)
            # Q(category__category__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if not request.user.is_authenticated():
        return redirect('login_or_register')
    else:

        form = ReviewForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            message = 'Please check and approve new review: "' + request.POST.get('review', '') \
                      + '" on http://www.goldenlisbon.com/admin/review/review/'
            subject = 'New review!'
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('review:list')

    context = {
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'nav': {
            'tour_categories_list': Category.objects.all(),
            'offer_categories_list': OfferCategory.objects.all(),
        },
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
            {'url': '/reviews', 'name': _('Reviews')},
            {'url': '#', 'name': category[0], 'active': True}
        ],
        'title': category[0],
        'object_list': queryset,
        'form': form,
        'value': _('Add'),
        'page_request_var': page_request_var
    }

    return render(request, 'partials/review_filter.html', context)


def review_delete(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Review, pk=pk)
    instance.delete()
    messages.success(request, 'Review deleted')
    return redirect('review:list')
