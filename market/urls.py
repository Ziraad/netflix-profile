from django.urls import path
from .views import shopping_cart, shopping_cart_add_items

app_name = 'market'

urlpatterns = [
    path('shopping/cart/', shopping_cart, name='shopping_cart'),
    path('shopping/cart/add_items/<slug:slug>/', shopping_cart_add_items, name='shopping_cart_add_items'),
    # path('shopping/cart/remove_items/', views.shopping_cart_remove_items, name='shopping_cart_remove_items'),
]
