from rest_framework.routers import DefaultRouter

from .views import (RatingViewSet,
                    CommentViewSet)

router = DefaultRouter()
router.register('ratings', RatingViewSet)
router.register('comments', CommentViewSet)


urlpatterns = router.urls

