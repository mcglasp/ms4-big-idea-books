from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<int:item_id>', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
    path('add_author/', views.add_author, name='add_author'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]
