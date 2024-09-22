from django.shortcuts import render
from .serializers import StorySerializer,StoryDetailSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Story,MemberActivity
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


import random


class StoryPagination(PageNumberPagination):
    page_size = 20
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
    

class StoryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, story_id, *args, **kwargs):
        try:
            story=Story.objects.get(id=story_id)

            story.views += 1
            story.save()


            serializer = StoryDetailSerializer(story)
            return Response(serializer.data, status =status.HTTP_200_OK)
        except Story.DoesNotExist:
            return Response({"detail":"Story not found"}, status=status.HTTP_404_NOT_FOUND)
       

class TrackingStartingReadingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, story_id, format=None):
        user = request.user
        try:
            story = Story.objects.get(id=story_id)
            
        except Story.DoesNotExist:
            return Response({"error":"Story not found"}, status=status.HTTP_404_NOT_FOUND)
        

        # Check if a reading session already existed, if not create it now

        activity, created = MemberActivity.objects.get_or_create(user=user, story=story)
        activity.start_reading = timezone.now()
        activity.save()

        return Response({
            "message":"Reading session is starting.",
            "duration": activity.duration
        }, status=status.HTTP_200_OK)
    
                


class TrackingEndReadingView(APIView):

    def post(self, request, story_id, format=None):
        user=request.user
        try:
            story=Story.objects.get(id=story_id)
        except Story.DoesNotExist:
            return Response({"error": "Story not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            activity = MemberActivity.objects.get(user=user, story=story, start_reading__isnull=False)

        except MemberActivity.DoesNotExist:
            return Response({"error":"No active reading session found"}, status=status.HTTP_400_BAD_REQUEST)
        

        activity.end_reading = timezone.now()
        activity.save()

        return Response({
            "message":"Reading session ended",
            "duration":activity.duration
        }, status=status.HTTP_200_OK)
        