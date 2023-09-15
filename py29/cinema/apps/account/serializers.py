from rest_framework import serializers
from django.contrib.auth import get_user_model

from .utils import send_code

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    password1 = serializers.CharField(min_length=8, max_length=128, required=True)
    first_name = serializers.CharField(max_length=150)

    def validate(self, attrs):
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError({'email': 'user with this email already exists'})

        if attrs.get('password') != attrs.pop('password1'):
            raise serializers.ValidationError({'password1': 'passwords did not match'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_code(user.email, user.code)
        return user


class ActivateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        if not User.objects.filter(email=attrs.get('email'), code=attrs.get('code')).exists():
            raise serializers.ValidationError('User not found with such email or code')

        return attrs

    def activate(self):
        user = User.objects.get(email=self.validated_data.get('email'), code=self.validated_data.get('code'))
        user.code = ''
        user.is_active = True
        user.save()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'get_full_name')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if not self.context.get('request').user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError({'old_password': 'incorrect'})

        if attrs.get('password') != attrs.pop('password1'):
            raise serializers.ValidationError({'password1': 'password did not match'})

        return attrs

    def set_new_password(self):
        self.context.get('request').user.set_password(self.validated_data.get('password'))
