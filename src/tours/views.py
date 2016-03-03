from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Tour, Offer, Contact


def tour_list(request):
    queryset_list = Tour.objects.all()
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

        'tour_list': queryset,
        'title': 'Tours',
        'breadcrumbs_list': breadcrumbs_list,
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/tours.html', context)


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'partials/detail.html'
    context_object_name = 'object'


class ServiceDetailView(generic.DetailView):
    model = Offer
    template_name = 'partials/detail.html'
    context_object_name = 'object'


class Edit(generic.edit.UpdateView):
    model = Tour
    template_name = 'partials/tour_form.html'
    fields = ['text', 'url', 'img']
    success_url = '/tours/'


class ContactEdit(generic.edit.UpdateView):
    model = Contact
    template_name = 'partials/contact_form.html'
    fields = ['first_name', 'last_name', 'img', 'category', 'mobile', 'email', 'whatsapp', 'viber', 'telegram', 'skype',
              'facebook', 'twitter', 'pinterest', 'google', 'instagram']
    success_url = '/contacts/'