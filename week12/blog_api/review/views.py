from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsActivePermission

from .models import Comment
from .serializers import CommentSerializer


# Create your views here.
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['update', 'retrieve', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsActivePermission]
        return super().get_permissions()

