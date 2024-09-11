from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Story
        fields=['id','title','type']
    
class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Story
        fields=['title','content','type','views','created_at']