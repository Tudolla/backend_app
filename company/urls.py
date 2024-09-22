from django.urls import path
from .views import CompanyInforView, ProjectListView, LeadershipListView, JobOpeningListView, MissionVisionView


urlpatterns = [
    path('company/<int:pk>/', CompanyInforView.as_view(), name='company-info'),
    path('company/<int:company_id>/projects/',ProjectListView.as_view(), name='project'),
    path('company/<int:company_id>/leadership/', LeadershipListView.as_view(), name='leadership'),
    path('company/<int:company_id>/job-openings/', JobOpeningListView.as_view(), name='job-opening'),
    path('company/<int:company_id>/mission-vision/', MissionVisionView.as_view(), name='mission-vision'),

]
