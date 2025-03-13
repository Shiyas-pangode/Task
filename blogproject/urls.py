from django.contrib import admin
from django.urls import path , include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/', include('blogapi.v1.auth.urls')),
    path('user/', include('blogapi.v1.users.urls')),
    path('postapi/', include('blogapi.v1.postapi.urls')),
    path('resetapi/', include('blogapi.v1.password.urls')),
]
