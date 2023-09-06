import uuid

from rest_framework import serializers
from slugify import slugify

from .models import Post, Category, Tag


class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('slug', 'title', 'body', 'author', 'image', 'category', 'tag', 'created_at', 'updated_at',)
        read_only_fields = ('author', 'created_at', 'updated_at',)

    def create(self, validated_data: dict):
        user = self.context.get('request').user
        validated_data.update({
            'author': user
        })
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update({
            'author': instance.author.email
        })

        return rep


class PostDetailSerializer(BasePostSerializer):
    ...


class PostSerializer(BasePostSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'slug', 'body', 'image')
        read_only_fields = ('author',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
