from django.db import models

from api.common import EmployeePositions, Services


class Specialist(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    position = models.CharField(max_length=255, choices=EmployeePositions.choices)
    photo = models.ImageField(max_length=255, upload_to='photos-of-specialists/')

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Service(models.Model):
    title = models.CharField(max_length=255, choices=Services.choices)
    description = models.CharField(max_length=1024, blank=True, null=True)
    cost = models.FloatField()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

