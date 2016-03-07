from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    model = Contact.objects.all()
    breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/contacts', 'name': 'Contacts'}]
    context = {
        'title': 'Contacts',
        'breadcrumbs_list': breadcrumbs_list,
        'contact_list': model,
    }

    return render(request, 'partials/contact.html', context)


def contact_detail(request, pk=None):
    breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/tours', 'name': 'Contact detail'}]
    model = Contact.objects.get(pk=pk)
    context = {
        'breadcrumbs_list': breadcrumbs_list,
        'title': 'Contact detail',
        'object': model,
    }

    return render(request, 'partials/detail.html', context)


def contact_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Contact Created')
            return redirect('contact:list')

        context = {
            'title': 'Contact create',
            'breadcrumbs_list': [{'url': '/', 'name': 'Home'}, {'url': '/tours', 'name': 'Contact create'}],
            'value': 'Contact create',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def contact_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/contacts', 'name': 'Contacts'}]
        instance = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Contact saved')
            return redirect('contact:list')

        context = {
            'title': 'Contact Edit',
            'breadcrumbs_list': breadcrumbs_list,
            'instance': instance,
            'form': form
        }
        return render(request, 'templates/_edit_form.html', context)


def contact_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    instance = get_object_or_404(Contact, pk=pk)
    instance.delete()
    messages.success(request, 'Contact deleted')
    return redirect('contact:list')
