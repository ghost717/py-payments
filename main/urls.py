from django.urls import path, include
from .views import platnosci, treningi, nt, et, dt, posts, newPost, editPost, deletePost, listingFilesInDir, listingFilesInDir2, postGallery, postGallery2
from django.contrib.auth import views as auth_views

#REST
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rest_posts', PostViewSet)

urlpatterns = [
    path('platnosci/', platnosci),
    path('treningi/', treningi),
    path('nt/', nt, name="nt"),
    path('et/<int:id>/', et, name="et"),
    path('dt/<int:id>/', dt, name="dt"),
    path('posts/', posts, name="posts"),
    path('newPost/', newPost, name="newPost"),
    path('editPost/<int:id>/', editPost, name="editPost"),
    path('deletePost/<int:id>/', deletePost, name="deletePost"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('postGallery/', postGallery, name="postGallery"),
    path('postGallery2/', postGallery2, name="postGallery2"),
    path('listingFilesInDir/', listingFilesInDir),
    path('listingFilesInDir2/', listingFilesInDir2),
    path('', include(router.urls)),
]