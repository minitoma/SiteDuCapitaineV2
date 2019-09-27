from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Projet

# Create your views here.

def projet_list(request):
    projets = Projet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projet/projet_list.html', {'projets': projets, 'nbar':'projets'})
