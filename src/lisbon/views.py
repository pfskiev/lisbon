from django.shortcuts import render
from offer.models import Offer
from tours.models import About


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


def login_or_register(request):
    return render(request, 'partials/login_or_register.html')
