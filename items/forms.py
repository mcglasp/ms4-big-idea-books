from django import forms
from .models import Item, Genre, Age_range, Author


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('sku', 'quantity_sold', 'discounted_price',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        screen_names = [(g.id, g.get_screen_name()) for g in genres]

        self.fields['genre'].choices = screen_names
