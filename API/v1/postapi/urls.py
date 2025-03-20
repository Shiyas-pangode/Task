from django.urls import path
from .views import PostCreatedView , PostRetrieveView  ,PostListView, BlogDetailView,PostListView
from . import views


urlpatterns = [

    path('post/', PostCreatedView.as_view(), name = 'create_post'), #postcreation
    path('post/posts/',PostListView.as_view(), name='post_list_search'), #post list view
    path('post/<int:pk>/', PostRetrieveView.as_view(), name = 'retrieve_single_view'),
    path('post//posts/?q=title' ,PostListView.as_view(), name='post_list_search'), #post search based on title
    path('post/<int:pk>/author/',BlogDetailView.as_view(),name = 'postDeleteUpdate'), #post update and delete filterd by author

]