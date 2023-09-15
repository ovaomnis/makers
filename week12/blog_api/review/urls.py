from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, RatingCreateUpdateDestroyViewSet

router = DefaultRouter()
router.register('comments', CommentsViewSet)
router.register('ratings', RatingCreateUpdateDestroyViewSet)

urlpatterns = router.urls

