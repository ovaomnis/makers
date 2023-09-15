from rest_framework.routers import DefaultRouter

from .views import (FilmViewSet,
                    CategoryViewSet)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('films', FilmViewSet)

urlpatterns = router.urls
