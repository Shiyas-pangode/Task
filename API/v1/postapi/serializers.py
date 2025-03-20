from django.contrib.auth.models import User

from rest_framework import serializers

from general.models import BlogModel



class BlogModelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta :
        model = BlogModel
        fields = ['id','name','title','author','created_at']
        read_only_fields = ['author' ,'created_at']