from rest_framework import serializers
from django.db.models import Avg

from .models import Post, Comment, Rating

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    likes = serializers.ReadOnlyField(source='owner.likes')
    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        comments = CommentSerializer(instance.comments.all(), many=True)
        rep = super().to_representation(instance)
        rep.update({
            'likes': instance.likes.filter(is_like=True).count(),
            'ratings': instance.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'],
            'comments': comments.data
        })

        return rep


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ("-rating",)

