from django.shortcuts import render
from django.views import generic
from tours.models import Offer, Contact


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


class ReviewPage(generic.TemplateView):
    template_name = 'partials/about.html'
