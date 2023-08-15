from django.contrib.auth import get_user_model
from rest_framework import serializers


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
