from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import redirect
from django.conf import settings

from tours.forms import BookNow


def booking_info(request):
    if request.method == 'GET':
        return redirect('home')
    if request.method == 'POST':
        form = BookNow(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] + ' BOOK REQUEST from ' + fullname + ', ' + 'phone: ' + phone + ', ' + 'email: ' + email
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
