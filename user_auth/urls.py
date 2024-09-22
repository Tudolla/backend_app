from django.urls import path
from .views import LoginView,MemberInfoView,UpdateProfileView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('profile/<int:id>/', MemberInfoView.as_view(), name='profile'),
    path('profile/<int:id>/update/', UpdateProfileView.as_view(), name='profile_update')
]