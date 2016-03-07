from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    model = Contact.objects.all()
    context = {
        'title': 'Contacts',
        'breadcrumbs_list': [
            {'url': '/', 'name': 'Home'},
            {'url': '#', 'name': 'Contacts', 'active': True}],
        'contact_list': model,
    }

    return render(request, 'partials/contact.html', context)


def contact_detail(request, pk=None):
    contact = Contact.objects.get(pk=pk)
    breadcrumbs_list = [
        {'url': '/', 'name': 'Home', 'active': False},
        {'url': '/contacts', 'name': 'Contacts', 'active': False},
        {'url': '#', 'name': contact.first_name + ' ' + contact.last_name, 'active': True}]
    context = {
        'breadcrumbs_list': breadcrumbs_list,
        'title': contact.first_name + ' ' + contact.last_name,
        'contact': contact,
    }

    return render(request, 'templates/_contact_details.html', context)


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
            'title': 'Contact creating',
            'breadcrumbs_list': [
                {'url': '/', 'name': 'Home', 'active': False},
                {'url': '/contacts', 'name': 'Contacts', 'active': False},
                {'url': '#', 'name': 'Contact creating', 'active': True}],
            'value': 'Contact creating',
            'form': form
        }

        return render(request, 'templates/_form.html', context)


def contact_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:signup')
    else:
        instance = get_object_or_404(Contact, pk=pk)
        breadcrumbs_list = [{'url': '/', 'name': 'Home'}, {'url': '/contacts', 'name': 'Contacts'},
                            {'url': '#', 'name': instance.first_name + ' ' + instance.last_name, 'active': True}]
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
