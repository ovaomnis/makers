from django.urls import path

from .views import get_post, put_patch_delete


urlpatterns = [
    path('', get_post),
    path('<slug:uuid>/', put_patch_delete)
]
