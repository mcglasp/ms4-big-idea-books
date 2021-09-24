from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<int:item_id>', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('deactivate_campaign/<int:campaign_id>/', views.deactivate_campaign, name='deactivate_campaign'),
    path('activate_campaign/<int:campaign_id>/', views.activate_campaign, name='activate_campaign'),
    path('manage_campaigns/', views.manage_campaigns, name='manage_campaigns'),
    path('update_campaign/<int:campaign_id>/', views.update_campaign, name='update_campaign'),
    path('delete_campaign/<int:campaign_id>/', views.delete_campaign, name='delete_campaign'),
    path('go_to_offer/<int:offer_id>/', views.go_to_offer, name='go_to_offer'),
    path('latest_items/', views.latest_items, name='latest_items'),
]
