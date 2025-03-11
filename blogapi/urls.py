from django.conf import settings
from django.urls import path
from .  import views 

from rest_framework_simplejwt.views import TokenRefreshView
from .views import  UserRegistrationView,UserLoginView ,PostCreatedView , PostDetailView ,PostUpdateDeleteView


urlpatterns = [
    path('registration/', UserRegistrationView.as_view() , name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('post/', PostCreatedView.as_view(), name = 'post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'postdetails'),
    path('post/<int:pk>/author/', PostUpdateDeleteView.as_view(),name = 'postDeleteUpdate')

]
