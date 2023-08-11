from rest_framework import serializers

from .models import Post
from apps.review.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = '__all__'
        # fields = ['body']
        # exclude = ['id']

    def to_representation(self, instance: Post):
        comments = CommentSerializer(instance.comments.all(), many=True)
        rep = super().to_representation(instance)
        rep.update({
            'comments': comments.data,
            'author': instance.author.username
        })
        return rep
