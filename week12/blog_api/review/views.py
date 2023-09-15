from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsActivePermission, IsAdminOrReadOnly
from post.permissions import IsAuthorOrAdminPermission

from .models import Comment, Like, Rating
from .serializers import CommentSerializer, RatingSerializer


# Create your views here.
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'get']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsActivePermission]
        return super().get_permissions()


class RatingCreateUpdateDestroyViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'partial_update']:
            self.permission_classes = [IsAuthorOrAdminPermission]
        return super().get_permissions()

    
