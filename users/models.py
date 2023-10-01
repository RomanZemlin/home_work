from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, verbose_name='Аватар')
    telegram = models.CharField(max_length=255, blank=True, null=True, verbose_name='Телеграм')
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
