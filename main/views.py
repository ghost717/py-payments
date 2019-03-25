from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Post, Images, Treningi
from .forms import PostForm, ImageForm, TreningiForm

import os
from django.conf import settings

#login
from django.contrib.auth.decorators import login_required

#REST
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer

#gallery
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
@login_required
def platnosci(request):
   
    # filmy = ['Titanic', 'Avatar', 'Bravehear']
    # filmy = Movie.objects.filter(id=3)
    platnosci = Payment.objects.all()
    subtotal = Payment.objects.count()
    value = Payment.objects.filter(valueType=-1)
    # valueType = Payment.objects.valueType

    subtotal = value#value * valueType

    return render(request, 'platnosci.html', {'platnosci': platnosci, 'suma': subtotal})

def treningi(request):

    treningi = Treningi.objects.all()
    total = Treningi.objects.count()

    return render(request, 'treningi.html', {'treningi': treningi, 'suma': total})

def nt(request):

    form = TreningiForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(treningi)

    return render(request, 'formPost.html', {'form': form}) 

def et(request, id):

    post = get_object_or_404(Treningi, pk=id)

    form = TreningiForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(treningi)

    return render(request, 'formPost.html', {'form': form}) 

def dt(request, id):

    post = get_object_or_404(Treningi, pk=id)

    if request.method == "POST":
        post.delete()

        return redirect(treningi)

    return render(request, 'accept.html', {'post': post}) 

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

@login_required
def postGallery(request):

    dir_name = 'test'
    path = os.path.join(settings.MEDIA_ROOT, dir_name)
    images = []

    for f in os.listdir(path):
        if f.endswith("jpg") or f.endswith("png"): # to avoid other files
            images.append("%s/%s" % (dir_name, f)) # images.append("%s%s/%s" % (settings.MEDIA_URL, dir_name, f)) # modify the concatenation to fit your neet
            
    totalImages = len(images)

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=totalImages)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            # for form in formset.cleaned_data:
            #     #this helps to not crash if the user   
            #     #do not upload all the photos
            #     if form:
            #         image = form['image']
            #         photo = Images(post=post_form, image=image)
            #         photo.save()
            #         messages.success(request, "Yeeew, check it out on the home page!")
            for i in images:
                image = i
                photo = Images(post=post_form, image=image)
                photo.save()
                messages.success(request, "Yeeew, check it out on the home page!")

            # return HttpResponseRedirect("/")
            return redirect(posts)
            
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())

    return render(request, 'test.html', {'postForm': postForm, 'formset': formset, 'images': images})

@login_required
def postGallery2(request):

    dir_name = 'test'
    path = os.path.join(settings.MEDIA_ROOT, dir_name)
    dirs = []
    images = []
    images2 = []

    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                dirs.append("%s" % (entry.name))
                newDir = entry.name
                subpath = os.path.join(path, entry.name)

                with os.scandir(subpath) as it:
                    for entry in it:
                        if entry.is_file():
                            images2.append("%s/%s/%s" % (dir_name, newDir, entry.name))

                            ImageFormSet = modelformset_factory(Images, form=ImageForm)
                            #'extra' means the number of photos that you can upload   ^
                            if request.method == 'POST':

                                postForm = PostForm(request.POST)
                                formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

                                if postForm.is_valid() and formset.is_valid():
                                    post_form = postForm.save(commit=False)
                                    post_form.user = request.user
                                    post_form.title = newDir
                                    post_form.save()

                                    for i in images2:
                                        image = i
                                        photo = Images(post=post_form, image=image)
                                        photo.save()
                                        messages.success(request, "Yeeew, check it out on the home page!")

                                        # return HttpResponseRedirect("/")
                                    return redirect(posts)
                                        
                                else:
                                    print(postForm.errors, formset.errors)
                            else:
                                postForm = PostForm()
                                formset = ImageFormSet(queryset=Images.objects.none())

    return render(request, 'test.html', {'postForm': postForm, 'formset': formset, 'dirs': dirs, 'images': images, 'images2': images2})

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



