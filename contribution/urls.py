from django.urls import path
from .views import TextPostCreateView

urlpatterns = [
    path('create-post/', TextPostCreateView.as_view(), name='create_post'),
]
