from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Painting

def painting_list(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 6)  # Show 6 paintings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', {'page_obj': page_obj})

def all_paintings(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 12)  # Show 12 paintings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/all_paintings.html', {'page_obj': page_obj})
