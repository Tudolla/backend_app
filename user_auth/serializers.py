from rest_framework import serializers
from django.contrib.auth.models import User 


# Serializer use for custom Model return , it need more by hand
# create a new instance of Member in here
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField() #write_only=True no need Response with password field




class UserProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'address','image','position']
         

