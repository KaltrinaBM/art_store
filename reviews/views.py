from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from paintings.models import Painting


# View for Creating the reviews
@login_required
def add_review(request, painting_id):
    painting = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.painting = painting
            review.user = request.user
            review.save()
            return redirect('painting_detail', painting_id=painting.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form,
                  'painting': painting})


# View for Updating the Reviews
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        messages.error(request, 'You are not allowed to edit this review.')
        return redirect('painting_detail', painting_id=review.painting.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('painting_detail', painting_id=review.painting.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form,
                  'review': review})


# View for Deleting the Reviews
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    painting = review.painting

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('painting_detail', painting_id=painting.id)

    return render(request, 'reviews/delete_review.html', {'review': review})
