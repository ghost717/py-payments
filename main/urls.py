from django.urls import path, include
from .views import platnosci

urlpatterns = [
    path('platnosci/', platnosci),
]