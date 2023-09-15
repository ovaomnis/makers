from django.db.models import Avg
from rest_framework import serializers

from .models import (Film,
                     Category)
from apps.feedback.serializers import (CommentSerializer)


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('slug',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        comments = CommentSerializer(instance.comments.all(), many=True)
        rep.update({
            'comments': comments.data,
            'like': instance.likes.count(),
            'rating': instance.rating.aggregate(avg_rate=Avg('rate'))['avg_rate']
        })
        return rep
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('slug',)
