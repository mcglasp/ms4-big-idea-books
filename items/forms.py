from django import forms
from .models import Item, Genre, Age_range, Author


class ItemForm(forms.ModelForm):
    # authors = forms.ModelChoiceField(queryset=Author.objects.all().order_by('surname'))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('sku', 'quantity_sold',)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        authors = Author.objects.all()
        age_ranges = Age_range.objects.all()
        genre_names = [(g.id, g.name) for g in genres]
        authors_surnames = [(a.id, a.surname_first()) for a in authors]
        age_ranges = [(a.id, a.age_range) for a in age_ranges]
        self.fields['genre'].choices = genre_names
        self.fields['author'].select = authors_surnames
        self.fields['age_range'].choices = age_ranges


class AuthorDataForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
