from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MovieListCreateViewSet, ActorModelViewSet


router = DefaultRouter()
router.register('movies', MovieListCreateViewSet)
router.register('actors', ActorModelViewSet)

urlpatterns = router.urls
