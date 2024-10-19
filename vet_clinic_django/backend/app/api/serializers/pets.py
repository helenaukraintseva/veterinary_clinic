from rest_framework import serializers

from api.models import Pet, Breed, Species, MedicalHistory
from api.serializers import ServiceSerializer


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['name']


class BreedSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer()

    class Meta:
        model = Breed
        fields = ['name', 'species']


class PetInfoSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Pet
        fields = ['name', 'gender', 'age', 'photo', 'breed']


class MedicalHistorySerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = MedicalHistory
        fields = ['diagnosis', 'visit_date', 'service']
