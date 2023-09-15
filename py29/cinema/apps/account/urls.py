from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (RegisterAPIView,
                    ActivateAPIView,
                    ChangePasswordAPIView,
                    MeAPIView)

urlpatterns = [
    path('me/', MeAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view()),
]