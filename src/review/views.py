from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from .models import Review
from .forms import ReviewForm
from helpers.models import Helpers


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def review_list(request):
    queryset_list = Review.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('Reviews'), 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
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

    form = ReviewForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if not request.user.is_authenticated():
            return redirect('login_or_register')
        else:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            send_mail('Hello!', 'Check new review!', 'kostiantyn.pidlisnyi@customertimes.com',
                      ['podlesny@outlook.com'], fail_silently=False)
            return redirect('review:list')

    context = {
        'company': get_company(),
        'review_list': queryset,
        'title': _('Reviews'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add Review'),
        'form': form,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/review.html', context)


def review_detail(request, pk=None):
    review = Review.objects.get(pk=pk)
    lang = get_lang(request)
    nav_bar = {
        'pt': PTNavigation.objects.get(id=1),
        'gb': GBNavigation.objects.get(id=1),
        'de': DENavigation.objects.get(id=1)
    }
    breadcrumbs = [
        {'url': '/', 'name': nav_bar[lang].home},
        {'url': '#', 'name': nav_bar[lang].review},
        {'url': '#', 'name': review.text, 'active': True}]

    context = {
        'company': get_company(),
        'nav': nav_bar[lang],
        'lang': lang,
        'breadcrumbs': breadcrumbs,
        'title': 'Review',
        'object': review,
    }

    return render(request, 'templates/_review_details.html', context)


def review_create(request):
    if not request.user.is_authenticated():
        return redirect('login_or_register')
    else:
        lang = get_lang(request)
        form = ReviewForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            send_mail('Hello!', 'Check new review!', 'kostiantyn.pidlisnyi@customertimes.com',
                  ['podlesny@outlook.com'], fail_silently=False)
            return redirect('review:list')

        context = {
            'company': get_company(),
            'lang': lang,
            'title': 'Review creating',
            'breadcrumbs': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/gallery', 'name': 'Review', 'active': False},
                {'url': '#', 'name': 'Review creating', 'active': True}],
            'value': 'Contact creating',
            'form': form
        }

    return render(request, 'templates/_form.html', context)


def review_update(request, pk=None):
    lang = get_lang(request)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Review, pk=pk)
        breadcrumbs = [
            {'url': '/', 'name': 'Home', 'active': False},
            {'url': '/gallery', 'name': 'Review', 'active': False},
            {'url': '#', 'name': instance.title, 'active': True}]
        form = ReviewForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Review saved')
            return redirect('review:list')

        context = {
            'company': get_company(),
            'lang': lang,
            'title': 'Review Edit',
            'breadcrumbs': breadcrumbs,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def review_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Review, pk=pk)
    instance.delete()
    messages.success(request, 'Review deleted')
    return redirect('review:list')
