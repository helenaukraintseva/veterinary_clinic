from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True, null=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


