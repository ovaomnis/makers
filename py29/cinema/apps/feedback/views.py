from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import (Comment,
                     Rating)
from .serializers import (CommentSerializer,
                          RatingSerializer)


# Create your views here.
class RatingViewSet(mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
