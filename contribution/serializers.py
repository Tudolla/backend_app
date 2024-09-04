from rest_framework import serializers
from .models import TextPost

class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ['id', 'title', 'description', 'created_at', 'is_activate', 'user']
