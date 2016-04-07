from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from tours.models import Tour

from helpers.models import Helpers

from tours.models import Category

from tours.forms import BookNow


def get_lang(request):
    lang = request.LANGUAGE_CODE
    return lang


def get_company():
    return Helpers.objects.get(id=1).company_name


def category_list(request, slug=None):
    footer = {
        'pt': Helpers.objects.get(id=1).about_footer_PT,
        'en': Helpers.objects.get(id=1).about_footer_EN,
        'de': Helpers.objects.get(id=1).about_footer_DE
    }
    queryset_list = Tour.objects.filter(category__url__contains=slug)
    lang = get_lang(request)
    query = request.GET.get('q')
    if query:
        if 'pt' in lang:
            queryset_list = queryset_list.filter(
                Q(title_PT__icontains=query) |
                Q(description_PT__icontains=query) |
                Q(category__category__icontains=query)
            ).distinct()
        else:
            if 'en' in lang:
                queryset_list = queryset_list.filter(
                    Q(title_EN__icontains=query) |
                    Q(description_EN__icontains=query) |
                    Q(category__category__icontains=query)
                ).distinct()
            else:
                if 'de' in lang:
                    queryset_list = queryset_list.filter(
                        Q(title_DE__icontains=query) |
                        Q(description_DE__icontains=query) |
                        Q(category__category__icontains=query)
                    )
    paginator = Paginator(queryset_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    category = Category.objects.filter(url__icontains=slug)
    if request.method == 'GET':
        form = BookNow()
    else:
        form = BookNow(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            subject = 'BOOK REQUEST from ' + fullname
            from_email = settings.EMAIL_HOST_USER
            to_list = settings.EMAIL_TO
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
                # send_mail('Subject here', message, settings.EMAIL_HOST_USER,
                #           ['podlesny@outlook.com'], fail_silently=True)
                # send_mail(subject=fullname, body=phone, message, ['podlesny@outlook.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tour:list')
        else:
            return redirect('tour:create')

    context = {
        'form': form,
        'footer': {
            'about': footer[lang],
        },
        'categories_list': Category.objects.all(),
        'breadcrumbs': [
            {'url': '/', 'name': _('Home')},
            {'url': '/', 'name': _('Tours')},
            {'url': '#', 'name': category[0], 'active': True}
        ],
        'title': _('category'),
        'object_list': queryset,
        'page_request_var': page_request_var,
        'value': _('Add'),
    }

    return render(request, 'templates/_tour_cat.html', context)
