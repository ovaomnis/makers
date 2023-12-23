from django.urls import path
from account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view())
]
