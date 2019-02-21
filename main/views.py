from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Post

import os

from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def platnosci(request):
   
    # filmy = ['Titanic', 'Avatar', 'Bravehear']
    # filmy = Movie.objects.filter(id=3)
    platnosci = Payment.objects.all()
    subtotal = Payment.objects.count()

    return render(request, 'platnosci.html', {'platnosci': platnosci, 'suma': subtotal})

#@login_required
def posts(request):

    posts = Post.objects.all()
    subtotal = Post.objects.count()

    return render(request, 'posts.html', {'posts': posts, 'suma': subtotal})

def listingFilesInDir(request):
    path = r"C:\serwer\htdocs\dev\python\paymentes\app\my-media\post"
    img_list = os.listdir(path)

    return render(request, 'gallery.html', {'images': img_list})



