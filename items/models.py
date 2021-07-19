from django.db import models
from .utils import create_new_sku


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=254)
    screen_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_screen_name(self):
        return self.screen_name
    

class Age_range(models.Model):
    age_range = models.CharField(max_length=254)

    def __str__(self):
        return self.age_range


class Author(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    surname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class Item(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True, default=create_new_sku)
    title = models.CharField(max_length=254)
    genre = models.ManyToManyField('Genre')
    author = models.ManyToManyField('Author')
    description = models.TextField()
    age_range = models.ManyToManyField(
        'Age_range')
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title
    
    # CREDIT karthikr Stack Overflow
    # def get_author(self):
        
    #     return "\n".join([a.authors_set for a in self.authors_set.all()])
        
       



    # CREDIT karthikr Stack Overflow
    # def get_age_range(self):
    #     return "\n".join([a.age_range for a in self.age_range.all()])





    
