from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import UserRegistrationView, MyInfoApi

users_patterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('my_info/', MyInfoApi.as_view(), name='my_info'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('users/', include(users_patterns)),
]
