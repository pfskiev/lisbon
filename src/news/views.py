from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import BadHeaderError
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from tours.models import Category
from helpers.models import Helpers
from .models import Article
from django.core.urlresolvers import reverse_lazy


from .forms import ArticleForm


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def news_list(request):
    lang = get_lang(request)
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
        'title': _('News'),
        'object_list': queryset,
        'breadcrumbs': breadcrumbs,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'partials/news.html', context)


def news_detail(request, pk=None):
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
        'footer': {
            'about': footer[lang],
            'icon': Helpers.objects.get(id=1).footer_icon
        },
        'categories_list': Category.objects.all(),
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
        'categories_list': Category.objects.all(),
        'company': get_company(),
        'title': _('Create Article'),
        'breadcrumbs': breadcrumbs,
        'value': _('Add'),
        'form': form
    }

    return render(request, 'templates/_form.html', context)


def news_update(request, pk=None):
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
        lang = get_lang(request)
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
            'categories_list': Category.objects.all(),
            'company': get_company(),
            'title': _('Edit') + ' ' + title[lang],
            'breadcrumbs': breadcrumbs,
            'instance': related_link,
            'form': form,
            'value': _('Add'),
        }
        return render(request, 'templates/_form.html', context)


def news_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Article, pk=pk)
    instance.delete()
    messages.success(request, 'Article deleted')
    return redirect('news:list')
