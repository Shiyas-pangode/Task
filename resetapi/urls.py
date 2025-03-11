from django.conf import settings
from django.urls import path
from .  import views 
from .views import PasswordResetView


urlpatterns = [

    path('reset/',PasswordResetView.as_view() , name='reset')
]