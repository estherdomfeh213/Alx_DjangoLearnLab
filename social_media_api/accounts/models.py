from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers_set', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_set')
    
    
class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['follower', 'following']  # Prevent a user from following the same person twice

    def __str__(self):
        return f'{self.follower} follows {self.following}'
