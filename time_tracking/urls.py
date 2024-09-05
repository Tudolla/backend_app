from django.urls import path
from .views import AttendanceForMonthView


urlpatterns = [
    path('attendance/<int:month>/<int:year>/', AttendanceForMonthView.as_view()),
]
