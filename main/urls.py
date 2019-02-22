from django.urls import path, include
from .views import platnosci, posts, newPost, editPost, deletePost, listingFilesInDir, listingFilesInDir2

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts),
    path('newPost/', newPost),
    path('editPost/<int:id>/', editPost),
    path('deletePost/<int:id>/', deletePost),
    path('listingFilesInDir/', listingFilesInDir),
    path('listingFilesInDir2/', listingFilesInDir2),
]