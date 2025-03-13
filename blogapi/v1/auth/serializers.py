from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from general.models import BlogModel
from django.contrib.auth import authenticate



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise serializers.ValidationError({"error": "Must include 'username' and 'password'."})

        user = authenticate(request=self.context.get('request') ,username=username, password=password)
        if not user:
            raise serializers.ValidationError({"error": "Unable to log in with provided credentials."})

        if not user.is_active:
            raise serializers.ValidationError({"error": "User account is inactive."})

      
        refresh = RefreshToken.for_user(user)

        return {
            'user': user,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
            

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
        
