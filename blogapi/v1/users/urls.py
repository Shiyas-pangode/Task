from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import UserRegistrationView 

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name = 'register'),
]
