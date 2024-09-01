from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone

class User(AbstractUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return self.username