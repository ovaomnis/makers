from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from .models import Post


# Create your views here.
class ListCreateView(APIView):
    def get(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()


class RetrieveUpdateDeleteView(APIView):
    def get(self, request: Request, slug: str):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def patch(self, request: Request, slug: str):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(instance=post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request: Request, slug: str):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return Response(f'Post with slug {slug} successfully deleted')
