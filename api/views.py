from django.shortcuts import render
from rest_framework.decorators import api_view

from api.serializers import CartItemSerializer, CartSerializer, CategoryDetailSerializer, CategoryListSerializer, ProductListSerializer, ProductDetailSerializer, ReviewSerializer
from .models import Cart, CartItem, Product, Category, Review
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serialize = ProductDetailSerializer(product)
    return Response(serialize.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    cart_code = request.data.get('cart_code')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    cart, created = Cart.objects.get_or_create(cart_code=cart_code)
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
    cart_item.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['PUT'])
def update_cart_item_quantity(request, cart_item_id):
    quantity = request.data.get('quantity')
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.quantity = int(quantity)
    cart_item.save()
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data)

@api_view(['POST'])
def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    rating = request.data.get('rating')
    review_text = request.data.get('review')

    if Review.objects.filter(product=product, user=user).exists():
        return Response({"error": "You have already reviewed this product."}, status=400)

    review = Review.objects.create(
        product=product,
        user=user,
        rating=rating,
        review=review_text
    )
    review.save()

    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(["PUT"])
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    rating = request.data.get("rating")
    review_text = request.data.get("review")

    review.rating = rating
    review.review = review_text
    review.save()

    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return Response({"message": "Review deleted successfully."}, status=204)
