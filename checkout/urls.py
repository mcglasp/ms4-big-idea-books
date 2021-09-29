from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'cache_checkout_data/', views.cache_checkout_data,
        name='cache_checkout_data'),
    path(
        'order_confirmation/<order_number>/',
        views.order_confirmation, name='order_confirmation'),
    path('wh/', webhook, name='webhook'),
]