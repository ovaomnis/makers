from rest_framework import serializers
from django.db.models import Avg

from .models import Post, Comment, Rating, PostImage

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = "__all__"

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    likes = serializers.ReadOnlyField(source='owner.likes')
    comments = CommentSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'likes': instance.likes.filter(is_like=True).count(),
            'ratings': instance.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'],
        })

        return rep

    def create(self, validated_data):
        post = super().create(validated_data)
        request = self.context.get('request')
        files = request.FILES

        image_objects = []
        for file in files.getlist('images'):
            image_objects.append(PostImage(post=post, image=file))

        PostImage.objects.bulk_create(image_objects)

        return post


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ("-rating",)





