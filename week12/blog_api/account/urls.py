from django.urls import path

from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='account_register'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout')
]
