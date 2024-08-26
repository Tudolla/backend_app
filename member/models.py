from django.db import models
import hashlib
# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique= True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', null=True, blank=True) # lưu ý kho image/

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.username
    
    def check_password(self, raw_password):
        return self.password == raw_password

    def set_password(self, raw_password):
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()
