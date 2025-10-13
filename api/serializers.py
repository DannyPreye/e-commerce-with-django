from rest_framework import serializers
from .models import Product , Category, Cart, CartItem

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name",  "price", "slug", "image_url", "category", "created_at", "updated_at"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name",  "description", "price", "slug", "image_url", "category", "created_at", "updated_at"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image_url", "products"]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image_url"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "created_at", "updated_at"]

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "sub_total", "created_at"]

    def get_sub_total(self, obj):
        return obj.product.price * obj.quantity

class  CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "items", "total", "created_at", "updated_at"]

    def get_total(self, obj):
        total = sum([item.product.price * item.quantity for item in obj.items.all()])
        return total

class CartStatsSerializer(serializers.ModelSerializer):
    total_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "total_items", "total_price", "created_at", "updated_at"]

    def get_total_items(self, obj):
        return sum([item.quantity for item in obj.items.all()])

    def get_total_price(self, obj):
        return sum([item.product.price * item.quantity for item in obj.items.all()])
