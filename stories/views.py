from django.shortcuts import render
from .serializers import StorySerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Story
from rest_framework.permissions import IsAuthenticated


import random


class StoryPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 20

class StoryListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail":"Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        

        stories = Story.objects.filter(type__in=['cuoi', 'tamlinh','khoahoc','ngungon'])

        if not stories.exists():
            return Response({"detail":"No stories found."}, status=status.HTTP_404_NOT_FOUND)

        story_list = list(stories)

        random.shuffle(story_list)

        paginator = StoryPagination()

        paginated_stories = paginator.paginate_queryset(story_list,request)


        serializer = StorySerializer(paginated_stories,many=True)

        return paginator.get_paginated_response(serializer.data)
    


