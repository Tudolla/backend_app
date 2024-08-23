from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Member
from .serializers import LoginSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            try:
                member = Member.objects.get(username=username)
            except Member.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            if member.check_password(password):
                refresh = RefreshToken.for_user(member)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'id':member.id,
                }
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class MemberInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, member_id):
        try:
            member = Member.objects.get(id=member_id)
            if member != request.user:
                return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)
            serializer = UserProfileSerializer(member)
            return Response(serializer.data)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)