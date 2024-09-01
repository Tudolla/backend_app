from django.urls import path
from .views import LoginView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    # path('profile/<int:member_id>/', MemberInfoView.as_view(), name='profile'),
    # path('profile/<int:member_id>/update/', MemberUpdateView.as_view(), name='profile_update')
]