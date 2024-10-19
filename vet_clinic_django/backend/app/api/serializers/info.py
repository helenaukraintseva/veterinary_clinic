from rest_framework import serializers

from api.models import Specialist, Service


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['first_name', 'second_name', 'experience', 'position', 'photo']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title', 'description', 'cost']
