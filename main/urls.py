from django.urls import path, include
from .views import platnosci, posts, newPost, editPost, deletePost, listingFilesInDir, listingFilesInDir2

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts, name="posts"),
    path('newPost/', newPost, name="newPost"),
    path('editPost/<int:id>/', editPost, name="editPost"),
    path('deletePost/<int:id>/', deletePost, name="deletePost"),
    path('listingFilesInDir/', listingFilesInDir),
    path('listingFilesInDir2/', listingFilesInDir2),
]