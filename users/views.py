from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from phonenumber_field.validators import validate_international_phonenumber

from users.models import User, PhoneSubmition


def send_sms(phone_number):
    phone_submition, created = PhoneSubmition.objects.get_or_create(phone=phone_number)
    

def login_or_register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('tel')
        if phone_number:
            try:
                validate_international_phonenumber[phone_number]
            except ValidationError:
                HttpResponse('invalid phone number')

            send_sms(phone_number)
            user, created = User.objects.get_or_create(phone=phone_number)
            

            if created:
                pass
