from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import BadHeaderError
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from tours.models import Category
from offer.models import OfferCategory
from helpers.models import Helpers
from .models import Article
from django.core.urlresolvers import reverse_lazy
from tours.forms import ContactMe
from .forms import ArticleForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def news_list(request):
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
    queryset_list = Article.objects.all()
    lang = get_lang(request)
    breadcrumbs = [
        {'url': '/', 'name': _('Home')},
        {'url': '#', 'name': _('News'), 'active': True}
    ]

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
        'title': _('News'),
        'object_list': queryset,
        'breadcrumbs': breadcrumbs,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'partials/news.html', context)


def news_detail(request, pk=None):
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
    article = Article.objects.get(pk=pk)
    title = {
        'pt': article.title_PT,
        'en': article.title_EN,
        'de': article.title_DE
    }
    description = {
        'pt': article.description_PT,
        'en': article.description_EN,
        'de': article.description_DE
    }
    lang = get_lang(request)
    breadcrumbs = [
        {'url': '/', 'name': _('Home'), 'active': False},
        {'url': '/news', 'name': _('News'), 'active': False},
        {'url': '#', 'name': title[lang], 'active': True}]

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
        'breadcrumbs': breadcrumbs,
        'title': title[lang],
        'object': {
            'id': article.id,
            'keywords_SEO': article.keywords_SEO,
            'description_SEO': article.description_SEO,
            'title': title[lang],
            'description': description[lang],
            'img': article.img,
        },
    }

    return render(request, 'templates/_news_details.html', context)


def news_create(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = ArticleForm(request.POST or None, request.FILES or None)
        breadcrumbs = [{'url': '/', 'name': _('Home'), 'active': False},
                       {'url': '/news', 'name': _('News'),
                        'active': False},
                       {'url': '#', 'name': _('Create Article'), 'active': True}]
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Article created')
            return redirect('news:list')

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
        'title': _('Create Article'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'templates/_form.html', context)


def news_update(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    lang = get_lang(request)
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        related_link = get_object_or_404(Article, pk=pk)
        title = {
            'pt': related_link.title_PT,
            'en': related_link.title_EN,
            'de': related_link.title_DE
        }
        breadcrumbs = [{'url': '/', 'name': _('Home')},
                       {'url': '/news', 'name': _('News')},
                       {'url': '#', 'name': _('Edit') + ' ' + title[lang], 'active': True}]
        form = ArticleForm(request.POST or None, request.FILES or None, instance=related_link)
        if form.is_valid():
            related_link = form.save(commit=False)
            related_link.save()
            messages.success(request, _('Article saved'))
            return redirect('news:list')

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
            'instance': related_link,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def news_delete(request, pk=None):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('search') + '?q=' + query)
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Article, pk=pk)
    instance.delete()
    messages.success(request, 'Article deleted')
    return redirect('news:list')
