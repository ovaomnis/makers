from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import RegistrationSerializer, ActivationSerializer

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
