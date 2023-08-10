from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('uuid', 'body', 'done', 'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'updated_at', 'uuid')
