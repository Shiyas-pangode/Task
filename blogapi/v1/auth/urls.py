from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import my_view , UserLoginView 


urlpatterns = [
    path('view/', my_view, name = 'view'),
    path('login/', UserLoginView.as_view(), name = 'user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



