from rest_framework.generics import ListAPIView
from api.models import Specialist, Service
from api.serializers import SpecialistSerializer, ServiceSerializer


class SpecialistListView(ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
