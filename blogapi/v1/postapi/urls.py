from django.urls import path
from .views import PostCreatedView , PostDetailView , search_posts , PostUpdateDeleteView
from . import views


urlpatterns = [
    path('post/', PostCreatedView, name = 'post'),
    path('post/<int:pk>/', PostDetailView, name = 'postdetails'),
    path('search/', search_posts, name='search'),
    path('post/<int:pk>/author/', PostUpdateDeleteView,name = 'postDeleteUpdate'),
]