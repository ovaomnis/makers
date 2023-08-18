from django.urls import path

from .views import PostListCreateView, PostRetrieveView, CategoryListCreateView, TagListCreateView


urlpatterns = [
    path('post/', PostListCreateView.as_view(), name='post_post_list_create'),
    # path('<slug:slug>/', RetrieveUpdateDeleteView.as_view(), name='post_retrieve_update_delete')
    path('post/<slug:pk>/', PostRetrieveView.as_view(), name='post_post_retrieve'),
    path('category/', CategoryListCreateView.as_view(), name='post_category_list_create'),
    path('tag/', TagListCreateView.as_view(), name='post_tag_list_create'),
]
