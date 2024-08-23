from rest_framework import serializers
from .models import Member

# Serializer use for custom Model return , it need more by hand
# create a new instance of Member in here
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



# ModelSerializer use for basic, convert all properties in Model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'username', 'email', 'address', 'position', 'image']
         