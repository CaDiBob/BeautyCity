from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User


class CustomUserManager(BaseUserManager):

    def create_user(self, phone='+70000000000', ot_password=None, username=None, password=None, **extra_fields):
        if not phone and not extra_fields.get('is_superuser'):
            raise ValueError('Не указан номер телефона')
        if not username:
            if ot_password == '1234':
                username = phone
                user = self.model(username=username, phone=phone, **extra_fields)
                user.set_password(super().make_random_password())
                user.save()
                return user
            raise ValueError('Код не подходит')
        else:
            user = self.model(username=username, phone=phone, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username=username, password=password, **extra_fields)

