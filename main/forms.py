from django.forms import ModelForm
from django import forms
from .models import Post, Images

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'thumbnail'] 

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ['image']