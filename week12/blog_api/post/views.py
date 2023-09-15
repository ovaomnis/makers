import django_filters.rest_framework
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins, viewsets, filters

from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, TagSerializer
from .models import Post, Category, Tag
from .permissions import IsAuthorOrAdminPermission
from accounts.permissions import IsAdminOrReadOnly


# Create your views here.
# class ListCreateView(APIView):
#     def get(self, request: Request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request: Request):
#         serializer = PostSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [IsAuthenticated()]
#         return super().get_permissions()
#
#
# class RetrieveUpdateDeleteView(APIView):
#     def get(self, request: Request, slug: str):
#         post = get_object_or_404(Post, slug=slug)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def patch(self, request: Request, slug: str):
#         post = get_object_or_404(Post, slug=slug)
#         serializer = PostSerializer(instance=post, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#
#     def delete(self, request: Request, slug: str):
#         post = get_object_or_404(Post, slug=slug)
#         post.delete()
#         return Response(f'Post with slug {slug} successfully deleted')


# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method in ['POST']:
#             return PostDetailSerializer
#         return PostSerializer
#
# class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#
# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class TagListCreateView(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['tag__title', 'category', 'author']
    search_fields = ['title', 'body']
    ordering_fields = ['-created_at', 'title']

    def get_serializer_class(self):
        if self.action != 'list':
            self.serializer_class = PostDetailSerializer
        else:
            self.serializer_class = PostSerializer
        return super().get_serializer_class()


    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAuthorOrAdminPermission]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly, ]
