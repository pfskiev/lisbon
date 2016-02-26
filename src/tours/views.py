from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from .models import Tour


def tour_list(request):
    queryset_list = Tour.objects.all()
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
        'page_request_var': page_request_var,
    }

    return render(request, 'partials/tours.html', context)


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'partials/detail.html'
    context_object_name = 'object'

