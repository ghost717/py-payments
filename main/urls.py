from django.urls import path, include
from .views import platnosci, posts, newPost, listingFilesInDir, listingFilesInDir2

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts),
    path('newPost/', newPost),
    path('listingFilesInDir/', listingFilesInDir),
    path('listingFilesInDir2/', listingFilesInDir2),
]