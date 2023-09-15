from rest_framework import serializers

from .models import Comment, Like, Rating


class LinkAuthorBase(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data.update({
            'author': user
        })
        return super().create(validated_data)


class CommentSerializer(LinkAuthorBase):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)


class RatingSerializer(LinkAuthorBase):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = 'author',

    def validate_rating(self, rating):
        if not 0 <= rating <= 10:
            raise serializers.ValidationError('rating only allowed between 0 and 10')
        return rating

    def validate_post(self, post):
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(author=user, post=post).exists():
            raise serializers.ValidationError('You already gave rating for this post')

        return post

