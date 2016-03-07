from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Offer
from .forms import OfferForm


def offer_list(request):
    queryset_list = Offer.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '#', 'name': 'Offers', 'active': True}
    ]
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
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

    context = {

        'title': 'Offers',
        'object_list': queryset,
        'breadcrumbs_list': breadcrumbs,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/offer.html', context)


def offer_detail(request, pk=None):
    offer = Offer.objects.get(pk=pk)
    breadcrumbs_list = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '/offers', 'name': 'Offers', 'active': False},
        {'url': '#', 'name': offer.title, 'active': True}]
    context = {
        'breadcrumbs_list': breadcrumbs_list,
        'title': offer.title,
        'offer': offer,
    }

    return render(request, 'templates/_offer_details.html', context)


def offer_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = OfferForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Offer Created')
            return redirect('offer:list')

        context = {
            'title': 'Offer creating',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/offers', 'name': 'Offers', 'active': False},
                {'url': '#', 'name': 'Offer creating', 'active': True}],
            'value': 'Offer creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def offer_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Offer, pk=pk)
        breadcrumbs_list = [{'url': '/', 'name': 'Home'},
                            {'url': '/offer', 'name': 'Offers'},
                            {'url': '#', 'name': instance.title, 'active': True}]
        form = OfferForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Offer saved')
            return redirect('offer:list')

        context = {
            'title': 'Offer Edit',
            'breadcrumbs_list': breadcrumbs_list,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def offer_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Offer, pk=pk)
    instance.delete()
    messages.success(request, 'Offer deleted')
    return redirect('offer:list')
