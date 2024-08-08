from django.shortcuts import render, get_object_or_404
from .models import Painting
from django.core.paginator import Paginator
from .forms import PaintingForm

def all_paintings(request):
    sort_by = request.GET.get('sort_by', 'title')  
    order = request.GET.get('order', 'asc') 

    if order == 'desc':
        sort_by = f'-{sort_by}'

    paintings = Painting.objects.all().order_by(sort_by)
    paginator = Paginator(paintings, 12) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
        'order': order,
    }
    
    return render(request, 'paintings/all_paintings.html', context)


# def all_paintings(request):
#     paintings = Painting.objects.all()
#     paginator = Paginator(paintings, 12)  # Show 12 paintings per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'paintings/all_paintings.html', {'page_obj': page_obj})

def painting_detail(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    return render(request, 'paintings/painting_detail.html', {'painting': painting})

def add_painting(request):
    """ Add a painting to the store """
    form = PaintingForm()
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_painting'))
        else:
            messages.error(request, 'Failed to add painting. Please ensure the form is valid.')
    else:
        form = PaintingForm()

    template = 'paintings/add_painting.html'
    context = {
        'form': form,
    }

    return render(request, template, context)