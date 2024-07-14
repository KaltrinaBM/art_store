from django.shortcuts import render, get_object_or_404
from .models import Painting

def painting_list(request):
    paintings = Painting.objects.all()
    return render(request, 'paintings/painting_list.html', {'paintings': paintings})

def painting_detail(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    return render(request, 'paintings/painting_detail.html', {'painting': painting})
    


def all_paintings(request):
    paintings = Painting.objects.all()
    context = {
        'page_obj': paintings
    }
    return render(request, 'paintings/all_paintings.html', context)
