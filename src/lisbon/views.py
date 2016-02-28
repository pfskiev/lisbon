from django.shortcuts import render
from django.views import generic
from tours.models import Offer


def home(request):
    context = {
        'offer_list': Offer.objects.all(),
    }

    return render(request, 'partials/home.html', context)


class AboutPage(generic.TemplateView):
    template_name = 'partials/about.html'


class PricingPage(generic.TemplateView):
    template_name = 'partials/about.html'
