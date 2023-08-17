from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=4)
    password = serializers.CharField(required=True, min_length=4)
    password_confirm = serializers.CharField(required=True, min_length=4)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'username already exists'
            )
        return username

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if not password == password_confirm:
            raise serializers.ValidationError(
                'Passwords not match'
            )

        return attrs

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username: str):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'User not found'
            )
        return username
    def validate(self, attrs):
        request = attrs.get('request')
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password, request=request)

            if not user:
                raise serializers.ValidationError(
                    'Provided credentials are incorrect'
                )

        else:
            raise serializers.ValidationError(
                'Email and Password required'
            )

        attrs['user'] = user
        return attrs

