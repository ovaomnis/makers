import uuid

from rest_framework import serializers
from slugify import slugify

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('slug', 'title', 'body', 'author', 'image', 'category', 'tag', 'created_at', 'updated_at',)
        read_only_fields = ('author', 'created_at', 'updated_at',)

    def validate(self, attrs: dict):
        title = attrs.get('title')
        if self.Meta.model.objects.filter(slug=slugify(title)).exists():
            attrs.update({
                'slug': f'{slugify(title)}-{uuid.uuid4().hex[:8]}'
            })
        return attrs

    def create(self, validated_data: dict):
        user = self.context.get('request').user
        validated_data.update({
            'author': user
        })
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'author': instance.author.username
        })

        return rep
