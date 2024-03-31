from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(**NULLABLE, verbose_name="email")
    first_name = models.CharField(max_length=150, **NULLABLE, verbose_name="имя")
    last_name = models.CharField(max_length=150, **NULLABLE, verbose_name="фамилия")

    phone = models.CharField(unique=True, max_length=35, verbose_name='номер телефона')
    code = models.CharField(**NULLABLE, max_length=4)
    invite_code = models.CharField(**NULLABLE, max_length=6)
    active_invite_code = models.CharField(**NULLABLE, max_length=6)
    phone_verify = models.BooleanField(default=False, verbose_name='верификация телефона')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
