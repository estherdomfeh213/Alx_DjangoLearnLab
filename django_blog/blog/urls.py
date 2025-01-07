from django.urls import path
from . import views
 
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.PostListView.as_view(), name='post_list'),  
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'), 
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),  

]
