from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils import timezone

from users.managers import CustomUserManager

class User(AbstractUser):

    phone = PhoneNumberField(
        'номер телефона',
        unique=True,
        default='+79993331100'
        )

    created_at = models.DateTimeField(
        default=timezone.datetime.now
        )

    objects = CustomUserManager()

    def __str__(self):
        return self.phone