
from django.urls import path
from .views import LoginView, MemberInfoView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('profile/<int:member_id>/', MemberInfoView.as_view(), name='profile')
]