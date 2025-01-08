from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['username'],
            validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', ''),
        )
        return user
