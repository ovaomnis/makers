from django.urls import path

from .views import post_list, create_post, delete_post, update_post


urlpatterns = [
    path('', post_list),
    path('create/', create_post),
    path('delete/<int:pk>/', delete_post),
    path('update/<int:pk>/', update_post),
]
