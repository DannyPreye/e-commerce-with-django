from .views import add_review, delete_review, product_list, product_detail, category_list, category_detail, add_to_cart, update_cart_item_quantity, update_review
from django.urls import path


urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<slug:slug>/', product_detail, name='product-detail'),
    path('categories/', category_list, name='category-list'),
    path('categories/<slug:slug>/', category_detail, name='category-detail'),
    path('cart/add/', add_to_cart, name='add-to-cart'),
    path('cart/item/<int:cart_item_id>/update/', update_cart_item_quantity, name='update-cart-item-quantity'),
    path("reviews/<int:product_id>", add_review, name="add-review"),
    path("reviews/<int:review_id>/update/", update_review, name="update-review"),
    path("reviews/<int:review_id>/delete/", delete_review, name="delete-review"),
]
