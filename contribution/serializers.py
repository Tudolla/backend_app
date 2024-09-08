from rest_framework import serializers
from .models import TextPost,PollPost, Choice

class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ['id', 'title', 'description', 'created_at', 'is_activate', 'user']



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields = ['id','choice_text','count']
class PollPostSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True) # Lồng choices vào Pollpost
    class Meta: 
        model = PollPost
        fields = ['id','created_at','is_activate','user','choices']

    def create(self, validated_data):
        # lấy danh sách các choices mà người dùng nhập vào đã valiate
        choices_data = validated_data.pop('choices')

        pollpost = PollPost.objects.create(**validated_data)

        for choice_data in choices_data: 
            Choice.objects.create(poll=pollpost, **choice_data) # poll ở đây chính là khóa ngoại ở Model

        return pollpost