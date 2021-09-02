from django.contrib import admin
from .models import Genre, Author, Age_range, Item

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class AgeRangeAdmin(admin.ModelAdmin):
    list_display = (
        'age_range',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'surname',
    )

    ordering = ('surname',)


class ItemAdmin(admin.ModelAdmin):

    def author_display(self, obj):
        author_list = []

        for author in obj.author.all():
            author_list.append(author)
        
        return author_list

    author_display.short_description = 'author/s'

    def genre_display(self, obj):
        genre_list = []

        for genre in obj.genre.all():
            genre_list.append(genre)
        
        return genre_list

    genre_display.short_description = 'genre/s'

    def age_range_display(self, obj):
        age_range_list = []

        for age_range in obj.age_range.all():
            age_range_list.append(age_range)
        
        return age_range_list

    age_range_display.short_description = 'age range/s'
        
    list_display = (
        'sku',
        'title',
        'image',
        'image_url',
        'description',
        'author_display',
        'genre_display',
        'age_range_display',
        'price',
        'discount',
        'set_sale_price',
        'final_price',
        'quantity_sold',
        'featured',
    )

    ordering = ('title',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Age_range, AgeRangeAdmin)
admin.site.register(Item, ItemAdmin)
