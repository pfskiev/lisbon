from django.shortcuts import render, redirect
from django.views import generic
from tours.models import Offer, Post, About
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

