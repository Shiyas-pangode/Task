from rest_framework.response import Response
from rest_framework import generics , permissions , status
from .serializers import BlogModelSerializer
from rest_framework.pagination import PageNumberPagination
from general.models import BlogModel
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Q




@api_view(['GET', 'POST'])
class PostCreatedView(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.IsAuthenticated]



    def perform_create(self , serializer):
        serializer.save(author=self.request.user)

    def get(self, request):
        posts = BlogModel.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5 
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BlogModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
class PostDetailView(generics.RetrieveAPIView):
    
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return BlogModel.objects.all()

@api_view(['GET'])
def search_posts(request):
    query = request.GET.get('q', '')  
    posts = BlogModel.objects.all()

    if query:
        posts = posts.filter(Q(title__icontains=query))  

    serializer = BlogModelSerializer(posts, many=True)  
    return Response({'query': query, 'results': serializer.data})

@api_view(['PUT', 'DELETE'])
class PostUpdateDeleteView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]  

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
   