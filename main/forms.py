from django.forms import ModelForm
from .models import Post, Images
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'thumbnail'] 

class ImageForm(ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ['image']