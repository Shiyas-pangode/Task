from rest_framework.response import Response
from rest_framework import generics , permissions , status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated ,AllowAny 

from django.shortcuts import get_object_or_404
from django.db.models import Q
from .permissions import IsAuthorOrReadOnly
from .serializers import BlogModelSerializer
from general.models import BlogModel


class PostCreatedView(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthenticated]



    def perform_create(self , serializer):
        serializer.save(author=self.request.user)

    def get(self, request):
        posts = BlogModel.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5 
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BlogModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PostRetrieveView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    
    serializer_class = BlogModelSerializer

    def get_queryset(self):
        return BlogModel.objects.all()



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticated]  

class PostListView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer

       
    def get_queryset(self):
        query = self.request.GET.get('q', '')  
        queryset = BlogModel.objects.all()

        if query:
            queryset = queryset.filter(Q(title__icontains=query))  
        
        return queryset
   