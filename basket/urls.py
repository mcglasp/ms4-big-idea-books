from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add_to_basket/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('update_quantity/<item_id>/', views.update_quantity, name='update_quantity'),
    path('remove_from_basket/<item_id>/', views.remove_from_basket, name='remove_from_basket'),
]