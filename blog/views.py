from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.core.paginator import Paginator
from django.db.models import Q

# View of the Blog Posts list with search option, including pagination
def blog_post_list(request):
    query = request.GET.get('q')
    posts = BlogPost.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        )

    paginator = Paginator(posts, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/blog_post_list.html', {'page_obj': page_obj})


# View of the Blog Post content
def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/blog_post_detail.html', {'post': post})
