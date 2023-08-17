from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .utils import send_activation_code


User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, required=True)
    password_confirm = serializers.CharField(min_length=4, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user with this email already exists')
        return email

    def validate(self, attrs: dict):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password_confirm != password:
            raise serializers.ValidationError({'password_confirm': 'Passwords not match'})
        return attrs

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)
        user.create_activation_code()
        send_activation_code(user.email, user.activation_code)
        return user


class ActivationSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    code = serializers.CharField(max_length=20, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')

        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError({'activation_code': 'Not valid activation code or email'})


        return attrs

    def activate(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.activation_code = ''
        user.save()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        return email

    def validate(self, attrs: dict) -> dict:
        request = attrs.get('request')
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password, request=request)

            if not user:
                raise serializers.ValidationError(
                    'Authentication Failed due to provided credentials'
                )
        else:
            raise serializers.ValidationError('Email and Password are required')

        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    def validate_old_password(self, old_password):
        user = self.context.get('request').user
        if not user.check_password(old_password):
            raise serializers.ValidationError('old password is not correct')
        return old_password

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        user = self.context.get('request').user

        if not new_password == new_password_confirm:
            raise serializers.ValidationError('Password confirmation error')

        if user.check_password(new_password):
            raise serializers.ValidationError('New password are same with previous')

        return attrs

    def set_new_password(self):
        new_password = self.validated_data.get('new_password')
        user = self.context.get('request').user
        user.set_password(new_password)
        user.save()


