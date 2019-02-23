from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Post
from .forms import PostForm

import os
from django.conf import settings


from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def platnosci(request):
   
    # filmy = ['Titanic', 'Avatar', 'Bravehear']
    # filmy = Movie.objects.filter(id=3)
    platnosci = Payment.objects.all()
    subtotal = Payment.objects.count()

    return render(request, 'platnosci.html', {'platnosci': platnosci, 'suma': subtotal})

def posts(request):

    posts = Post.objects.all()
    subtotal = Post.objects.count()

    return render(request, 'posts.html', {'posts': posts, 'suma': subtotal})

@login_required
def newPost(request):

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(posts)

    return render(request, 'formPost.html', {'form': form}) 

@login_required
def editPost(request, id):

    post = get_object_or_404(Post, pk=id)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(posts)

    return render(request, 'formPost.html', {'form': form}) 

@login_required
def deletePost(request, id):

    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        post.delete()

        return redirect(posts)

    return render(request, 'accept.html', {'post': post}) 

def listingFilesInDir(request):
    path = r"C:\serwer\htdocs\dev\python\paymentes\app\my-media\post"
    img_list = os.listdir(path)

    return render(request, 'gallery.html', {'images': img_list})

def listingFilesInDir2(request):
    dir_name = 'post'
    path = os.path.join(settings.MEDIA_ROOT, dir_name)
    images = []
    for f in os.listdir(path):
        if f.endswith("jpg") or f.endswith("png"): # to avoid other files
            images.append("%s%s/%s" % (settings.MEDIA_URL, dir_name, f)) # modify the concatenation to fit your neet
    
    return render(request, 'gallery.html', {'images': images})



