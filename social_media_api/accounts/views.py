from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework.views import APIView
from .serializers import CustomUser
from .models import Follow 



class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            return Response({
                'token': token.key,
                'username': user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Fetch the user to follow
        try:
            user_to_follow = CustomUser.objects.all()
            
            # Check if the user is already following
            if user_to_follow in request.user.following.all():
                return Response({"message": f"You are already following {user_to_follow.username}"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Add user to the following list
            request.user.following.add(user_to_follow)
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Fetch the user to unfollow
        try:
            user_to_unfollow = CustomUser.objects.all()
            
            # Check if the user is not following the other user
            if user_to_unfollow not in request.user.following.all():
                return Response({"message": f"You are not following {user_to_unfollow.username}"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Remove user from the following list
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

