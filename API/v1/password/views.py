from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PasswordResetSerializer




class PasswordResetView(generics.UpdateAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]  

    def get_object(self):
        return self.request.user  

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)