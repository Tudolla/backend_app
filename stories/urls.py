from django.urls import path
from .views import StoryListAPIView,TrackingStartingReadingView,TrackingEndReadingView,StoryDetailAPIView


urlpatterns = [
    path('stories/', StoryListAPIView.as_view(), name='stories-list'),
    path('story/<int:story_id>/', StoryDetailAPIView.as_view(), name='story-detail'),
    path('start-reading/<int:story_id>/',TrackingStartingReadingView.as_view(), name='start-reading'),
    path('end-reading/<int:story_id>/',TrackingEndReadingView.as_view(), name='end-reading' ),
]
