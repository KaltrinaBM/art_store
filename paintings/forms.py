from django import forms
from .widgets import CustomClearableFileInput
from .models import Painting


class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_title, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
