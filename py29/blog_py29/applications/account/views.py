from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией', status=201)


class ActivateAPIView(APIView):
    def get(self, request: Request, activation_code) -> Response:
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=('is_active', 'activation_code'))
        return Response('Вы успешно активировали аккаунт', status=200)

# class LoginAPIView(ObtainAuthToken):
#     serializer_class = LoginSerializer


# class LogoutAPIView(APIView):
#
#     permission_classes = [IsAuthenticated]
#     def post(self, request: Request) -> Response:
#         Token.objects.get(user=self.request.user).delete()
#         return Response('Приходите еще!')

