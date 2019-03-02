from django.forms import ModelForm
from django import forms
from .models import Post, Images, Treningi

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'thumbnail'] 

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ['image']

class TreningiForm(forms.ModelForm):
    class Meta:
        model = Treningi
        fields = ['title', 'description', 'date', 'ex01', 'ex02', 'ex03', 'ex04', 'ex05', 'ex06', 'ex07', 'ex08', 'ex09', 'ex10'] 