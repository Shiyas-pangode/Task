from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from general.models import BlogModel




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    email = serializers.CharField(write_only=True, style = {'input_type':'email'})
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        

        if not username or not password or not email:
            raise serializers.ValidationError({"error": "Must include 'username' , 'password' and 'email'."})

        user = authenticate(request=self.context.get('request') ,username=username, password=password , email = email)
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
        
