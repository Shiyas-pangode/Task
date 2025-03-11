from django.shortcuts import render
from .models import BlogModel

from .serializers import UserSerializer , LoginSerializer , TokenSerializer ,BlogModelSerializer

from rest_framework import generics, permissions, status
from .permissions import IsAuthorOnly 
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import RetrieveAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView


from django.http import HttpResponse
from django.shortcuts import get_object_or_404






# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)



class UserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "user": serializer.validated_data["user"].username,
            "refresh": serializer.validated_data["refresh"],
            "access": serializer.validated_data["access"],
        }, status=status.HTTP_200_OK)

class PostCreatedView(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self , serializer):
        serializer.save(author=self.request.user)


# class PostCreatedView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
#     queryset = BlogModel.objects.all()
#     serializer_class = BlogModelSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAuthorOnly]  # Only author can update/delete

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
class PostUpdateDeleteView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def put(self, request, pk):
        
        post = get_object_or_404(BlogModel, pk=pk)

        if post.author != request.user:
            return Response({"error": "You can only update your own posts."}, status=status.HTTP_403_FORBIDDEN)

        serializer = BlogModelSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
       
        post = get_object_or_404(BlogModel, pk=pk)

        if post.author != request.user:
            return Response({"error": "You can only delete your own posts."}, status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class PostDetailView(generics.RetrieveAPIView):
    
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlogModel.objects.all()
    
