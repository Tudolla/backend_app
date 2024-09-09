from django.urls import path
from .views import ActivatedPostListView, TextPostCreateView,PollPostCreateView,GetActivatedPollPostView,VotePollPostView

urlpatterns = [
    path('create-post/', TextPostCreateView.as_view(), name='create_post'),
    path('get-activated-posts/', ActivatedPostListView.as_view(), name='get_post'),
    path('create-pollpost/', PollPostCreateView.as_view(), name='create_pollpost'),
    path('get-pollpost/', GetActivatedPollPostView.as_view(), name='get_pollpost'),
    path('vote-pollpost/<int:choice_id>/', VotePollPostView.as_view(), name='vote_pollpost'),


]
