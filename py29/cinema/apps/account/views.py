from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (RegisterSerializer,
                          ActivateSerializer,
                          UserSerializer,
                          ChangePasswordSerializer)

# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('', status=201)


class ActivateAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ActivateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response('', status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, reqeust: Request) -> Response:
        serializer = ChangePasswordSerializer(data=reqeust.data, context={'request': reqeust})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('', status=200)


class MeAPIView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request: Request) -> Response:
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)
