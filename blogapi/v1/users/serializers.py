from rest_framework import serializers
from django.contrib.auth.models import User
from general.models import BlogModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def validate(self, data): 
    
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data
    
    def create(self, validated_data):
    
        password = validated_data.pop('password')  
        validated_data.pop('password2', None)  

        
        user = User.objects.create_user(**validated_data, password=password)
        return user

            
