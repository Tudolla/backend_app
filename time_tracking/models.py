from django.db import models
from django.conf import settings


class Attendance(models.Model):
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    date = models.DateField()
    status = models.CharField(max_length=10) # "Present" or "Absent"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'attendace'

    def __str__(self):
        return f"{self.user} - {self.date}"
    