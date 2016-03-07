from django.conf import settings
from django.conf.urls import url
from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.views import generic
from tours.models import Offer, Post, Gallery, About
from .forms import PostForm


def home(request):
    context = {
        'offer_list': Offer.objects.all(),
    }

    return render(request, 'partials/home.html', context)


def about(request):

    context = {
        'title': 'About Us',
        'about_list': About.objects.all()
    }

    return render(request, 'partials/about.html', context)


def review_list(request):

    context = {
        'title': 'Reviews',
        'review_list': Post.objects.all(),
    }

    return render(request, 'partials/review.html', context)


def gallery_list(request):
    queryset_list = Gallery.objects.all()
    breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/tours', 'name': 'Tours'}]
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {

        'object_list': queryset,
        'title': 'Gallery',
        'breadcrumbs_list': breadcrumbs_list,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/gallery.html', context)


def feedback_create(request):
    if not request.user.is_authenticated():
        return redirect('accounts:signup')

    else:
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            #  messages.success(request, "Successfully Created")
            return redirect('review_list')
        return render(request, 'partials/review_form.html', {"form": form})


class feedback_edit(generic.DetailView):
    model = Post
    template_name = 'partials/detail.html'
    context_object_name = 'object'

