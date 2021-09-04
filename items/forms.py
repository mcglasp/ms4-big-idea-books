from django import forms
from django.forms import ModelChoiceField
from .widgets import CustomClearableFileInput
from .models import Item, Genre, Age_range, Author


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('sku', 'quantity_sold', 'image_url')
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        age_ranges = Age_range.objects.all()
        genre_names = [(g.id, g.name) for g in genres]
        age_ranges = [(a.id, a.age_range) for a in age_ranges]
        self.fields['genre'].choices = genre_names
        self.fields['age_range'].choices = age_ranges


class AuthorDataForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
