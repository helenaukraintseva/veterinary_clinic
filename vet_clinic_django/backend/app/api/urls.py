from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import UserRegistrationView, UserInfoApi, SpecialistListView, ServiceListView, PetInfoApi, \
    MedicalHistoryApi

pets_patterns = [
    path('pet_info/', PetInfoApi.as_view(), name='pet_info'),
    path('medical_history/', MedicalHistoryApi.as_view(), name='medical_history')
]

info_patterns = [
    path('specialists/', SpecialistListView.as_view(), name='specialists'),
    path('services/', ServiceListView.as_view(), name='services')
]

users_patterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('user_info/', UserInfoApi.as_view(), name='user_info'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('users/', include(users_patterns)),
    path('info/', include(info_patterns)),
    path('pets/', include(pets_patterns))
]
