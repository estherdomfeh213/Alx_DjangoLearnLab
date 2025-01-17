from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.conf import settings

# Define the Post model dynamically using apps.get_model() to avoid circular imports

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']  # Prevent multiple likes from the same user on one post

    def __str__(self):
        return f'{self.user} liked {self.post.title}'

    
# class Notification(models.Model):
#     recipient = models.ForeignKey(CustomUser, related_name="notifications", on_delete=models.CASCADE)
#     actor = models.ForeignKey(CustomUser, related_name="actor_notifications", on_delete=models.CASCADE)
#     verb = models.CharField(max_length=255)
#     target_object_id = models.PositiveIntegerField()
#     target = GenericForeignKey('target_content_type', 'target_object_id')
#     timestamp = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.actor} {self.verb} {self.target}'

