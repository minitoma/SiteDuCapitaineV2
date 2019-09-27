from django.shortcuts import render
from django.utils import timezone
from projet.models import Projet


def home(request):
	last_project = Projet.objects.latest('published_date')
	return render(request,'home.html', {'last_project':last_project})
