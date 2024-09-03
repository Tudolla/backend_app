from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import TextPost

class TextPostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user)  

        if request.user.is_anonymous:
           return Response({"error": "User must be logged in."}, status=status.HTTP_401_UNAUTHORIZED)
        # Lấy dữ liệu từ request
        title = request.data.get('title')
        description = request.data.get('description')
        is_activate = request.data.get('is_activate', False)  # Giá trị mặc định là False nếu không có

        # Kiểm tra dữ liệu
        if not title or not description:
            return Response({"error": "Title and description are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Tạo đối tượng TextPost và lưu vào cơ sở dữ liệu
        text_post = TextPost.objects.create(
            title=title,
            description=description,
            is_activate=is_activate,
            user=request.user
        )

        # Tạo từ điển Python chứa dữ liệu của TextPost để trả về response
        response_data = {
            "id": text_post.id,
            "title": text_post.title,
            "description": text_post.description,
            "created_at": text_post.created_at,
            "is_activate": text_post.is_activate,
            "user_id": text_post.user.id,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
