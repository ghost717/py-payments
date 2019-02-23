from django.urls import path, include
from .views import platnosci, posts, newPost, editPost, deletePost, listingFilesInDir, listingFilesInDir2
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts, name="posts"),
    path('newPost/', newPost, name="newPost"),
    path('editPost/<int:id>/', editPost, name="editPost"),
    path('deletePost/<int:id>/', deletePost, name="deletePost"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('listingFilesInDir/', listingFilesInDir),
    path('listingFilesInDir2/', listingFilesInDir2),
]