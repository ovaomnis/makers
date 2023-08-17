from django.urls import path

from .views import ListCreateView, RetrieveUpdateDeleteView


urlpatterns = [
    path('', ListCreateView.as_view(), name='post_list_create'),
    path('<slug:slug>/', RetrieveUpdateDeleteView.as_view(), name='post_retrieve_update_delete')
]
