from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username or self.telegram_id
