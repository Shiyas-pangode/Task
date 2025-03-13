from rest_framework import serializers
from django.contrib.auth.models import User
from general.models import BlogModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
            




class BlogModelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta :
        model = BlogModel
        fields = ['id','name','title','author','created_at']
        read_only_fields = ['author' ,'created_at']