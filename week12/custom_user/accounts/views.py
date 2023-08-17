from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .permissions import IsActivePermission
from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer

# Create your views here.
User = get_user_model()

class RegistrationView(APIView):
    def post(self, request: Request):
        serializer = RegistrationSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def post(self, request: Request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Account Successfully activated', status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsActivePermission]

    def post(self, request: Request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response(
            'Successfully Logout'
        )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, IsActivePermission]

    def post(self, request: Request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Password has successfully changed')
