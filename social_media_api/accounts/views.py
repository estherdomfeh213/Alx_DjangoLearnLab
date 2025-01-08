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


# @api_view(['POST'])
# def follow_user(request, user_id):
#     user_to_follow = get_user_model().objects.get(id=user_id)
#     if user_to_follow != request.user:
#         request.user.following.add(user_to_follow)
#         return Response({"message": "Followed successfully"}, status=200)
#     return Response({"message": "You cannot follow yourself"}, status=400)

# @api_view(['POST'])
# def unfollow_user(request, user_id):
#     user_to_unfollow = get_user_model().objects.get(id=user_id)
#     request.user.following.remove(user_to_unfollow)
#     return Response({"message": "Unfollowed successfully"}, status=200)

CustomUser = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the user to follow
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Ensure that the user isn't following themselves
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Add user_to_follow to the current user's following list
        request.user.following.add(user_to_follow)
        return Response({"message": f"Successfully followed user {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the user to unfollow
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Ensure that the user isn't unfollowing themselves
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Remove user_to_unfollow from the current user's following list
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"Successfully unfollowed user {user_to_unfollow.username}"}, status=status.HTTP_200_OK)


class UserFollowingListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get all users that the current user is following
        following = request.user.following.all()
        following_list = [{"id": user.id, "username": user.username} for user in following]
        return Response({"following": following_list}, status=status.HTTP_200_OK)


class UserFeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get posts from users that the current user is following
        following = request.user.following.all()
        posts = []
        for user in following:
            user_posts = user.posts.all()  # Assuming the Post model is related to the user
            posts.extend(user_posts)

        # Sort posts by creation date (most recent first)
        posts = sorted(posts, key=lambda post: post.created_at, reverse=True)
        posts_list = [{"id": post.id, "title": post.title, "content": post.content, "author": post.author.username} for post in posts]

        return Response({"feed": posts_list}, status=status.HTTP_200_OK)
