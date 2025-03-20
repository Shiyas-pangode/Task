from django.urls import path
from .views import PostCreatedView , PostRetrieveView  ,PostListView, BlogDetailView,PostListView
from . import views


urlpatterns = [

    path('post/', PostCreatedView.as_view(), name = 'create_post'),
    path('post/<int:pk>/', PostRetrieveView.as_view(), name = 'retrieve_single_view'),
    path('posts/',PostListView.as_view(), name='post_list_search'),
    path('post/<int:pk>/author/',BlogDetailView.as_view(),name = 'postDeleteUpdate'),

]