from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activation/', ActivationView.as_view(), name='activation')
]
