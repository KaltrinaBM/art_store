from django import forms
from .models import Review


# Form for Creating reviews
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is None:
            raise forms.ValidationError("Rating cannot be empty.")
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
