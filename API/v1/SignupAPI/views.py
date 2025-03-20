
from rest_framework import generics ,permissions
from rest_framework.views import APIView

from .serializers  import UserSerializer 
from rest_framework.response import Response  
from rest_framework.decorators import api_view

from general.models import BlogModel




class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]




