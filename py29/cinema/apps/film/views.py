from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import IsAdminOrReadOnly
from .models import (Film,
                     Category)
from .serializers import (FilmSerializer,
                          CategorySerializer)

from apps.feedback.models import (Like)


# Create your views here.
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('film__title', 'slug',)
    search_fields = ('film__title', 'film__description',)
    ordering_fields = ('film__title',)

    @action(detail=True, methods=['POST'])
    def like(self, request: Request, pk) -> Response:

        if not Like.objects.filter(film__pk=pk, author=self.request.user).exists():
            like = Like(author=self.request.user, film=self.get_object())
            like.save()

        return Response('')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
