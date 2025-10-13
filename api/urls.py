from .views import product_list, product_detail, category_list, category_detail, add_to_cart, update_cart_item_quantity
from django.urls import path


urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<slug:slug>/', product_detail, name='product-detail'),
    path('categories/', category_list, name='category-list'),
    path('categories/<slug:slug>/', category_detail, name='category-detail'),
    path('cart/add/', add_to_cart, name='add-to-cart'),
    path('cart/item/<int:cart_item_id>/update/', update_cart_item_quantity, name='update-cart-item-quantity'),
]
