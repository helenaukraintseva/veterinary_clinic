from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.business_logic import get_pet_by_user, get_medical_history_by_pet
from api.serializers import PetInfoSerializer, MedicalHistorySerializer


class PetInfoApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pet = get_pet_by_user(request.user)
        serializer = PetInfoSerializer(pet)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicalHistoryApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pet_id: str = request.query_params.get('pet_id')
        medical_history = get_medical_history_by_pet(pet_id)
        serializer = MedicalHistorySerializer(medical_history, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
