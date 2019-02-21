from django.urls import path, include
from .views import platnosci, posts, listingFilesInDir

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts),
    path('listingFilesInDir/', listingFilesInDir),
]