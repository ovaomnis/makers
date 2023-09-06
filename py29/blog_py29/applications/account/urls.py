from django.urls import path

from applications.account.views import (RegisterAPIView,
                                        ActivateAPIView,
                                        LoginAPIView,
                                        LogoutAPIView)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
