
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_app.settings')
django.setup()


from django.contrib.auth.hashers import make_password
from user_auth.models import User


users = User.objects.all()

for user in users:
    current_password = user.password 
    hashed_password = make_password(current_password)
    user.password = hashed_password
    user.save()
    print("Mat khau thanh cong!")