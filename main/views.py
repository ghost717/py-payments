from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
# from .forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def platnosci(request):
   
    # filmy = ['Titanic', 'Avatar', 'Bravehear']
    # filmy = Movie.objects.filter(id=3)
    platnosci = Payment.objects.all()
    return render(request, 'platnosci.html', {'platnosci': platnosci})

#@login_required