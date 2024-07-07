from django.shortcuts import render
from .models import Painting

def painting_list(request):
    paintings = Painting.objects.all()
    return render(request, 'home/index.html', {'paintings': paintings})