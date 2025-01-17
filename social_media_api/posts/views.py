from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.apps import apps



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        # Serialize and return the posts
        return Response(PostSerializer(posts, many=True).data)
    
    
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        like = Like.objects.create(user=request.user, post=post)

        # Create notification for post like
        Notification = apps.get_model('notifications', 'Notification')  # Lazy import of Notification
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
        post = Post.objects.get(id=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)