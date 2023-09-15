from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import (ListPostView,
#                     RetrievePostView,
#                     CreatePostView,
#                     UpdatePostView,
#                     DeletePostView)
from .views import (PostViewSet,
                    CommentViewSet,
                    ImageModelViewSet)


router = DefaultRouter()
router.register('image', ImageModelViewSet)
router.register('comment', CommentViewSet)
router.register('', PostViewSet, basename='post')


urlpatterns = [
    # path('', include(router.urls))
    # path('create/', CreatePostView.as_view()),
    # path('<int:pk>/', RetrievePostView.as_view()),
    # path('<int:pk>/update/', UpdatePostView.as_view()),
    # path('<int:pk>/delete/', DeletePostView.as_view())
]

urlpatterns += router.urls