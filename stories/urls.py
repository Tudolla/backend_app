from django.urls import path
from .views import StoryListAPIView


urlpatterns = [
    path('stories/', StoryListAPIView.as_view(), name='stories-list')
]
