from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password field
        user = get_user_model().objects.create_user(**validated_data)  # Create user instance
        user.set_password(password)  # Set the password securely
        user.save()  # Save the user instance
        # Create and return the token after user is created
        token, created = Token.objects.get_or_create(user=user)
        return user, token


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = get_user_model().objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError("Invalid credentials")
