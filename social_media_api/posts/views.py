from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from posts.models import Post, Like

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the Post object
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post, and prevent them from doing so again
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for the like action
        content_type = ContentType.objects.get_for_model(post)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=content_type,
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the Post object
        post = get_object_or_404(Post, pk=pk)

        # Attempt to find the Like object, and delete it if it exists
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
