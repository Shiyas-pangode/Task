from django.contrib import admin
from django.urls import path , include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('API.v1.SigninAPI.urls')),
    path('user/', include('API.v1.SignupAPI.urls')),
    path('postapi/', include('API.v1.postapi.urls')),
    path('resetapi/', include('API.v1.password.urls')),
    
  
]
