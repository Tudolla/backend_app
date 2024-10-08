from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(request,username=username, password=password)
            if user is not None:
                try:
                    member = User.objects.get(id=user.id)
                except User.DoesNotExist:
                    return Response({'Error': "Member khong tim thay"}, status=status.HTTP_401.UNAUTHORIZED)
                
                refresh = RefreshToken.for_user(user)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'id': member.id,
                    'image': member.image.url if member.image else None,
                    'name': member.name,
                    'email': member.email,
                }
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect username or password'}, status=status.HTTP_401_UNAUTHORIZED)
      
class MemberInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            member = User.objects.get(id=id)
            member_data = {
                "id": member.id,
                "name": member.name,
                "username": member.username,
                "email": member.email,
                "address": member.address,
                "image": member.image.url if member.image else None,
                "position": member.position,
            }
            return Response(member_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    paser_classed= (MultiPartParser, FormParser) # xử lý các yêu câu tải tệp từ Clien

    def put(self, request, id):
        try:
            member = User.objects.get(id=id)

            member.name = request.data.get('name', member.name)
            member.username = request.data.get('username',member.username)
            member.email = request.data.get('email', member.email)
            member.address = request.data.get('address', member.address)
            member.position=request.data.get('position',member.position)

            if 'image' in request.FILES:
                member.image =request.FILES['image']
        
            member.save()



            member_data = {
              "id": member.id,
              "name":member.name,
              "username":member.username,
              "email":member.email,
              "address":member.address,
              "image":member.image.url if member.image else None,
              "position": member.position,
            }

            return Response(member_data,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    
