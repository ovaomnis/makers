from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password')
]
