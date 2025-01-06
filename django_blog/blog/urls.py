from django.urls import path
from . import views 
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View single post
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit an existing post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete a post,
]
