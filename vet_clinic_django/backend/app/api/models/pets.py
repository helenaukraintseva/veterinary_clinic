from django.db import models

from .users import User
from .info import Service
from api.common import PetGenders, PetSpecies


class Species(models.Model):
    name = models.CharField(max_length=255, choices=PetSpecies.choices)

    class Meta:
        verbose_name = 'Вид питомца'
        verbose_name_plural = 'Виды питомцев'


class Breed(models.Model):
    name = models.CharField(max_length=255)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='breed_species')

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Pet(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=PetGenders.choices)
    age = models.PositiveIntegerField()
    photo = models.ImageField(max_length=255, upload_to='photos-of-pets/', blank=True, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, related_name='pet_breed', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pet_user')

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'


class MedicalHistory(models.Model):
    diagnosis = models.CharField(max_length=1024)
    visit_date = models.DateField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_history_pet')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='medical_history_service')

    class Meta:
        verbose_name = 'История болезни'
        verbose_name_plural = 'История болезней'
