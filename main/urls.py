from django.urls import path, include
from .views import platnosci, posts

urlpatterns = [
    path('platnosci/', platnosci),
    path('posts/', posts),
]