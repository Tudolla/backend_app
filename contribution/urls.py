from django.urls import path
from .views import ActivatedPostListView, TextPostCreateView

urlpatterns = [
    path('create-post/', TextPostCreateView.as_view(), name='create_post'),
    path('get-activated-posts/', ActivatedPostListView.as_view(), name='get_post'),


]
