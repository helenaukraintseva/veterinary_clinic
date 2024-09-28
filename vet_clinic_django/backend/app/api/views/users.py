from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from api.models import User
from api.serializers import UserRegistrationSerializer
from api.serializers import UserInfoSerializer


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        context = dict(
            message='User registered successfully',
            code=status.HTTP_201_CREATED
        )

        return Response(context, status=status.HTTP_201_CREATED)


class MyInfoApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
