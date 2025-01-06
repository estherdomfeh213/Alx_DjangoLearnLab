from django import forms
from django.contrib.auth.models import User
from .models import Profile
from.models import Post

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content']