from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)


    def create(self, validated_data: dict):
        user = self.context.get('request').user
        validated_data.update({
            'author': user
        })
        return super().create(validated_data)


