from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer


# Create your views here.
class MovieListCreateViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorModelViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer