from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils import timezone

from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    phone = PhoneNumberField(
        'номер телефона',
        unique=True,
        region='RU',
        db_index=True
        )

    created_at = models.DateTimeField(
        default=timezone.datetime.now
        )

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.phone
