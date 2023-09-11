from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        print(instance)

        return super().to_representation(instance)
