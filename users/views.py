from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from phonenumber_field.validators import validate_international_phonenumber

from users.models import User, PhoneSubmition


def send_sms(phone_number):
    phone_submition, created = PhoneSubmition.objects.get_or_create(phone=phone_number)
    

def login_or_register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('tel')
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        if phone_number:
            try:
                validate_international_phonenumber[phone_number]
            except ValidationError:
                HttpResponse('invalid phone number')
            request.session['phone_number'] = phone_number
            user, created = User.objects.get_or_create(phone=phone_number)
            send_sms(phone_number)
            
            
        if num1 and num2 and num3 and num4:
            code_front = f'{num1}{num2}{num3}{num4}'
            user = authenticate(phone_number=request.session.get('phone_number'), ot_pass=code_front)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('project:index'))

                
                

