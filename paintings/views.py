from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Painting
from django.core.paginator import Paginator
from .forms import PaintingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


def painting_detail(request, painting_id):
    """ View to display a single painting """
    painting = get_object_or_404(Painting, pk=painting_id)
    context = {
        'painting': painting
    }
    return render(request, 'paintings/painting_detail.html',
                  {'painting': painting})


@login_required
def add_painting(request):
    """ Add a painting to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    form = PaintingForm()
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save()
            messages.success(request, 'Successfully added painting!')
            return redirect(reverse('painting_detail', args=[painting.id]))
        else:
            messages.error(request, 'Failed to add painting.'
                           'Please ensure the form is valid.')
    else:
        form = PaintingForm()

    template = 'paintings/add_painting.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_painting(request, painting_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    painting = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated painting!')
            return redirect(reverse('painting_detail', args=[painting.id]))
        else:
            messages.error(request, 'Failed to update painting.'
                           'Please ensure the form is valid.')
    else:
        form = PaintingForm(instance=painting)
        messages.info(request, f'You are editing { painting.title }')

    template = 'paintings/edit_painting.html'
    context = {
        'form': form,
        'painting': painting,
    }

    return render(request, template, context)


@login_required
def delete_painting(request, painting_id):
    """ Delete a painting from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    painting = get_object_or_404(Painting, pk=painting_id)
    painting.delete()
    messages.success(request, 'Painting deleted!')
    return redirect(reverse('all_paintings'))
