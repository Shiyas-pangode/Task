from django.urls import path
from .views import PostCreatedView , PostDetailView , search_posts , PostUpdateDeleteView
from . import views


urlpatterns = [
    path('post/', PostCreatedView.as_view(), name = 'post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'postdetails'),
    path('search/', search_posts, name='search'),
    path('post/<int:pk>/author/', PostUpdateDeleteView.as_view(),name = 'postDeleteUpdate'),
]