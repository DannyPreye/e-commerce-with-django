from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

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
