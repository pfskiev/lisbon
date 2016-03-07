from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Review
from .forms import ReviewForm


def review_list(request):
    queryset_list = Review.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '#', 'name': 'Reviews', 'active': True}
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

    context = {

        'review_list': queryset,
        'title': 'Review',
        'breadcrumbs_list': breadcrumbs,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/review.html', context)


def review_detail(request, pk=None):
    review = Review.objects.get(pk=pk)
    breadcrumbs = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '/reviews', 'name': 'Review', 'active': False},
        {'url': '#', 'name': review.title, 'active': True},
        ]
    context = {
        'breadcrumbs_list': breadcrumbs,
        'title': review.title,
        'object': review,
    }

    return render(request, 'templates/_review_details.html', context)


def review_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('login_or_register')
    else:
        form = ReviewForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Review Created')
            return redirect('review:list')

        context = {
            'title': 'Review creating',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/gallery', 'name': 'Review', 'active': False},
                {'url': '#', 'name': 'Review creating', 'active': True}],
            'value': 'Contact creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def review_update(request, pk=None):
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
            'title': 'Review Edit',
            'breadcrumbs_list': breadcrumbs,
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


