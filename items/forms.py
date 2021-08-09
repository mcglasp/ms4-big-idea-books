from django import forms
from .models import Item, Genre, Age_range, Author


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('sku', 'quantity_sold',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        authors = Author.objects.all()
        screen_names = [(g.id, g.get_screen_name()) for g in genres]
        authors_surnames = [(a.id, a.surname_first()) for a in authors]
        self.fields['genre'].choices = screen_names
        self.fields['author'].choices = authors_surnames


class AuthorDataForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
