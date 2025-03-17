from django.http import HttpResponse

from rest_framework import generics , permissions , status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LoginSerializer , TokenSerializer
from general.models import BlogModel

def my_view(request):
    return HttpResponse('hello')


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