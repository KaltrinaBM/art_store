from django.core.paginator import Paginator
from django.shortcuts import render
from paintings.models import Painting
from django.db.models import Q
from blog.models import BlogPost
import random

def home(request):
    query = request.GET.get('q', '')
    if query:
        paintings = Painting.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        all_paintings = list(Painting.objects.all())
        if len(all_paintings) > 3:
            paintings = random.sample(all_paintings, 3)
        else:
            paintings = all_paintings
    latest_blog_post = BlogPost.objects.order_by('-created_at').first()

    context = {
        'paintings': paintings,
        'query': query,
        'latest_blog_post': latest_blog_post,
    }
    return render(request, 'home/index.html', context)

def index(request):
    paintings = Painting.objects.order_by('?')[:3]
    context = {
        'paintings': paintings,
    }
    return render(request, 'home/index.html', context)


def painting_list(request):
    paintings = Painting.objects.all()
    paginator = Paginator(paintings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', {'page_obj': page_obj})


def all_paintings(request):
    sort_by = request.GET.get('sort_by', 'title')  # Default sort by title
    order = request.GET.get('order', 'asc')  # Default order ascending

    if order == 'desc':
        sort_by = f'-{sort_by}'

    paintings = Painting.objects.all().order_by(sort_by)
    paginator = Paginator(paintings, 12)  # Show 12 paintings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
        'order': order,
    }
    
    return render(request, 'paintings/all_paintings.html', context)
