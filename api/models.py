from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from ecommerceApi import settings

# Create your models here.

class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image_url = models.ImageField(upload_to='category_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)
    image_url = models.ImageField(upload_to='products_image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cart(models.Model):
        cart_code = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.cart_code

class CartItem(models.Model):
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
        quantity = models.PositiveIntegerField(default=1)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.quantity} of {self.product.name} in cart {self.cart.cart_code}"

class Review(models.Model):
     RATING_CHOICES = [
          (1, '1 Poor'),
          (2, '2 Fair'),
          (3, '3 Good'),
          (4, '4 Very Good'),
          (5, '5 Excellent'),
     ]

     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
     rating = models.PositiveIntegerField(choices=RATING_CHOICES)
     review = models.TextField(blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
            return f"Review of {self.product.name} by {self.user.username}"
     class Meta:
            # Ensure a user can only leave one review per product
            unique_together = ['product', 'user']
            ordering = ['created_at']

class ProductRating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='rating')
    average_rating = models.FloatField(default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rating for {self.product.name} - {self.average_rating} ({self.total_reviews} reviews)"

