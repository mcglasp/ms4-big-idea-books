from django import forms
from django.forms import ModelChoiceField
from .widgets import CustomClearableFileInput
from .models import Item, Genre, Age_range, Author
from django.core.exceptions import ValidationError



class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('sku', 'quantity_sold', 'image_url', 'final_price', 'date_added',)
    
    image = forms.ImageField(required=True, widget=CustomClearableFileInput)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        age_ranges = Age_range.objects.all()
        genre_names = [(g.id, g.name) for g in genres]
        age_ranges = [(a.id, a.age_range) for a in age_ranges]
        self.fields['genre'].choices = genre_names
        self.fields['age_range'].choices = age_ranges
        self.fields['featured'].widget.attrs.update({'class': 'custom-tickbox'})
        self.fields['featured'].label = "<span class='bold'>Featured?</span> <span class='italic'> Tick this box to feature this product on the home page  </span>"
        self.fields['genre'].label = "<span class='bold'>Genre</span> <span class='italic'> Hold down Cmd to select more than one  </span>"
        self.fields['genre'].required = True
        self.fields['age_range'].label = "<span class='bold'>Target age</span> <span class='italic'> Hold down Cmd to select more than one  </span>"
        self.fields['discount'].label = "<span class='bold'>Discount in %</span> <span class='italic'> Enter a percentage </span>"
        self.fields['set_sale_price'].label = "<span class='bold'>Fixed sale price</span> <span class='italic'> Enter a fixed sale amount to override any discount applied  </span>"
        self.fields['title'].label = "<span class='bold'>Title </span>"
        self.fields['description'].label = "<span class='bold'>Description  </span>"
        self.fields['price'].label = "<span class='bold'>Price  </span>"
        self.fields['price'].widget.attrs['min'] = 0.00
        self.fields['price'].widget.attrs['min'] = 0.00
        self.fields['set_sale_price'].widget.attrs['min'] = 0.00
        self.fields['set_sale_price'].required = False
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['default'] = 0
        self.fields['discount'].required = False
        self.fields['image'].label = "<span class='bold'>Select an image  </span>"    






class AuthorDataForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
