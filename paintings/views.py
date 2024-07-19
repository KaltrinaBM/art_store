from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Painting

def painting_list(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', {'page_obj': page_obj})

# def all_paintings(request):
#     sort_by = request.GET.get('sort_by', 'title')
#     order = request.GET.get('order', 'asc')
#     order_prefix = '' if order == 'asc' else '-'
#     paintings = Painting.objects.all().order_by(f'{order_prefix}{sort_by}')
#     paginator = Paginator(paintings, 12)  
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#         'sort_by': sort_by,
#         'order': order
#     }
#     return render(request, 'home/all_paintings.html', context)

def all_paintings(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 12)  # Show 12 paintings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'paintings/all_paintings.html', {'page_obj': page_obj})

def painting_detail(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    return render(request, 'paintings/painting_detail.html', {'painting': painting})