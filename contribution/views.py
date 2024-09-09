from django.utils import timezone 
from django.shortcuts import render
from .serializers import TextPostSerializer,PollPostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TextPost,Choice,PollPost

class TextPostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # print(request.user)  

        if request.user.is_anonymous:
           return Response({"error": "User must be logged in."}, status=status.HTTP_401_UNAUTHORIZED)
        # Lấy dữ liệu từ request
        title = request.data.get('title')
        description = request.data.get('description')
        is_activate = request.data.get('is_activate', False)  # Giá trị mặc định là False nếu không có

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

class PollPostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args, **kwargs):
        if request.user.is_anonymous:
           return Response({"error": "User must be logged in."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = PollPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ActivatedPostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Lọc bài viết đã được kích hoạt
        today = timezone.now().date()
        # sử dụng __date để lọc bài post = today,
        posts = TextPost.objects.filter(is_activate=True, created_at__date=today)
        
        # Serialize dữ liệu
        serializer = TextPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class GetActivatedPollPostView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request, *args,**kwargs):

        # Loc bai viet duoc kich hoat do Admin kiem soat
        today = timezone.now().date()

        # Loc các bài viết được kích hoạt và tạo hôm này 

        polls = PollPost.objects.filter(is_activate=True, created_at__date=today)

        # serialize dữ liệu trả về JSON

        serializer = PollPostSerializer(polls, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class VotePollPostView(APIView):
    def post(self, request, choice_id):
        try:
            choice = Choice.objects.get(id=choice_id)
        
        except Choice.DoesNotExist:
            return Response({'error':'Choice not found'}, status=status.HTTP_404_NOT_FOUND)
        

        choice.count +=1
        choice.save()

        return Response({'message':'Your vote is successful'}, status=status.HTTP_200_OK)
    