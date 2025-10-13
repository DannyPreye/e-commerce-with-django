from django.shortcuts import render
from rest_framework.decorators import api_view

from api.serializers import CartItemSerializer, CartSerializer, CategoryDetailSerializer, CategoryListSerializer, ProductListSerializer, ProductDetailSerializer
from .models import Cart, CartItem, Product, Category
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
