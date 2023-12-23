from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.utils import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate_email(self, email):
        return email

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password2 = serializers.CharField(required=True, min_length=6)

    def validate(self, attrs):
        user = self.context.get('request').user
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        new_password2 = attrs.get('new_password2')

        if new_password != new_password2:
            raise serializers.ValidationError('Password did not match')

        if not user.check_password(old_password):
            raise serializers.ValidationError('Old password did not match')

        attrs['user'] = user

        return attrs

    def set_new_password(self):
        user = self.validated_data.get('user')
        user.set_password(self.validated_data.get('new_password'))
        user.save()

