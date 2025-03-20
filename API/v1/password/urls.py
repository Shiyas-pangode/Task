from django.urls import path
from .  import views 
from .views import PasswordResetView


urlpatterns = [

    path('resetpassword/',PasswordResetView.as_view(), name='reset_password'),
    
]