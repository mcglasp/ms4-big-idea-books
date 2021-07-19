from django.contrib import admin
from .models import Genre, Author, Age_range, Item

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'screen_name',
        'name',
    )

    ordering = ('screen_name',)


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

    list_display = (
        'sku',
        'title',
        'image',
        'description',
    )

    ordering = ('title',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Age_range, AgeRangeAdmin)
admin.site.register(Item, ItemAdmin)
