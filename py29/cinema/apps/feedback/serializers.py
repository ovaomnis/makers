from rest_framework import serializers

from .models import (Comment,
                     Like,
                     Rating)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Comment
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(min_value=1, max_value=10)
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = "__all__"

    def create(self, validated_data: dict):
        user = self.context.get('request').user
        instance, _ = self.Meta.model.objects.get_or_create(author=user, film=validated_data.get('film'))
        instance.rate = validated_data.get('rate')
        instance.save()
        return instance

