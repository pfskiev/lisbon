from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from tours.forms import BookNow
from tours.forms import ContactMe


@require_http_methods(['POST'])
def booking_info(request):
    form = BookNow(request.POST)
    if form.is_valid():
        fullname = form.cleaned_data['fullname']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        message = form.cleaned_data[
                      'message'] + ' BOOK REQUEST from ' + fullname + ', ' + 'phone: ' + phone + ', ' + 'email: ' + email
        subject = 'BOOK REQUEST from ' + fullname + ', ' + 'phone: ' + phone + ', ' + 'email: ' + email
        from_email = settings.EMAIL_HOST_USER
        to_list = settings.EMAIL_TO
        try:
            send_mail(subject, message, from_email, to_list, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('tour:success')
    else:
        return redirect('tour:fail')


@require_http_methods(['POST'])
def contact(request):
    contact_me = ContactMe(request.POST)
    if contact_me.is_valid():
        fullname = contact_me.cleaned_data['fullname']
        message = contact_me.cleaned_data['message']
        subject = 'Mail from ' + fullname
        from_email = settings.EMAIL_HOST_USER
        to_list = settings.EMAIL_TO
        try:
            send_mail(subject, message, from_email, to_list, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('tour:success')
    else:
        return redirect('tour:fail')
