from django.core.checks import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from tours.models import Offer, Contact, Post, Gallery
from .forms import PostForm


def home(request):
    context = {
        'offer_list': Offer.objects.all(),
    }

    return render(request, 'partials/home.html', context)


class AboutPage(generic.TemplateView):
    template_name = 'partials/about.html'


def contact_list(request):
    context = {
        'contact_list': Contact.objects.all(),
    }

    return render(request, 'partials/contact.html', context)


def review_list(request):
    context = {
        'review_list': Post.objects.all(),
    }

    return render(request, 'partials/review.html', context)


def gallery_list(request):
    context = {
        'gallery_list': Gallery.objects.all(),
    }

    return render(request, 'partials/gallery.html', context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        # messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'partials/review_form.html', context)


